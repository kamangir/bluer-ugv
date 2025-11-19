from typing import List, Optional
import subprocess
import shlex
import time
from enum import Enum, auto

from bluer_options.logger import crash_report
from bluer_options.logger.config import log_list
from bluer_objects.graphics.screen import get_size
from bluer_objects import file

from bluer_ugv.logger import logger


class VideoPlayerEngine(Enum):
    MPV = auto()
    VLC = auto()

    def play_command(
        self,
        filename: str,
        fullscreen: bool = True,
        loop: bool = False,
        audio: bool = False,
    ) -> str:
        screen_height, screen_width = get_size()
        logger.info(
            "screen size: {}x{}".format(
                screen_height,
                screen_width,
            )
        )

        if self == VideoPlayerEngine.MPV:
            logger.info('press "q" to quit mpv.')

            return " ".join(
                [
                    "mpv",
                    "--no-border",
                    "--background=color",  # fill empty areas with black
                    "--keepaspect=yes",
                    "--no-keepaspect-window",
                    "--geometry=0:0",
                    (f"--autofit={screen_width}x{screen_height}" if fullscreen else ""),
                    "--loop" if loop else "",
                    "--no-audio" if not audio else "",
                    shlex.quote(filename),
                ]
            )

        if self == VideoPlayerEngine.VLC:
            logger.info('press "Enter" to quit vlc.')

            return " ".join(
                [
                    "sudo -u pi",
                    "cvlc",
                    "--fullscreen",  # true fullscreen
                    "--no-video-title-show",  # remove the title overlay
                    "--video-on-top",  # stay above desktop
                    "--no-osd",  # remove VLC overlays
                    "--loop" if loop else "",
                    "--no-audio" if not audio else "",
                    "--extraintf rc",  # remote control, to enable "quit"
                    f"--rc-host=127.0.0.1:41940",
                    shlex.quote(filename),
                ]
            )

        return "this-should-not-happen"


class VideoPlayer:
    def __init__(
        self,
        dryrun: bool = False,
        engine: VideoPlayerEngine = VideoPlayerEngine.VLC,
    ):
        self.process: Optional[subprocess.Popen] = None
        self.current_file: Optional[str] = None

        self.paused = False
        self.dryrun = dryrun

        assert engine in VideoPlayerEngine, f"{engine}: engine not found"
        self.engine: VideoPlayerEngine = engine

        logger.info(
            "{} created on {}{}.".format(
                self.__class__.__name__,
                self.engine.name.lower(),
                " [dryrun]" if dryrun else "",
            )
        )

    def pause(self) -> bool:
        if not self.dryrun:
            if self.process and self.process.poll() is None:
                try:
                    # mpv understands "p" as toggle-pause.
                    self.process.stdin.write(b"p")
                    self.process.stdin.flush()
                except Exception as e:
                    logger.error(f"failed to send pause command: {e}")
                    return False

        logger.info(
            "{}.{}".format(
                self.__class__.__name__, "resume" if self.paused else "pause"
            )
        )
        self.paused = not self.paused

        return True

    def play(
        self,
        filename: str,
        loop: bool = False,
        audio: bool = False,
        fullscreen: bool = True,
        verbose: bool = True,
    ) -> bool:
        if not file.exists(filename):
            logger.error(f"file not found: {filename}")
            return False

        # Kill previous playback if running
        self.stop()

        comand = self.engine.play_command(
            filename=filename,
            fullscreen=fullscreen,
            loop=loop,
            audio=audio,
        )
        logger.info(f"running on {self.engine.name.lower()}: {comand}")

        if not self.dryrun:
            try:
                # pylint: disable=consider-using-with
                self.process = subprocess.Popen(
                    shlex.split(comand),
                    stdin=None,
                    stdout=None if verbose else subprocess.DEVNULL,
                    stderr=None if verbose else subprocess.DEVNULL,
                )

                logger.info(
                    f"pid={self.process.pid}, "
                    f"stdin={self.process.stdin}, returncode={self.process.returncode}"
                )

            except Exception as e:
                crash_report(f"failed to run mpv: {e}")
                self.process = None
                return False

            if not self.process:
                logger.error("process is None.")
                return False

        self.current_file = filename

        logger.info(
            "{}.play({}{})".format(
                self.__class__.__name__,
                "loop: " if loop else "",
                filename,
            )
        )

        return True

    def play_list(
        self,
        playlist: List[str],
    ):
        log_list(
            logger,
            "play list",
            playlist,
            "filename(s)",
        )

        while True:
            for filename in playlist:
                self.play(filename, loop=False)

                # Wait until video finishes
                if self.process:
                    self.process.wait()

    def stop(self) -> bool:
        if not self.dryrun:
            if self.process and self.process.poll() is None:

                # MPV: try clean quit via stdin
                if self.engine == VideoPlayerEngine.MPV:
                    try:
                        if self.process.stdin:
                            self.process.stdin.write(b"q")
                            self.process.stdin.flush()
                        else:
                            logger.info("mpv: no stdin; skipping quit.")
                    except Exception as e:
                        logger.warning(f"mpv quit failed: {e}")

                # VLC: quit through RC Unix socket
                elif self.engine == VideoPlayerEngine.VLC:
                    try:
                        import socket

                        s = socket.create_connection(("127.0.0.1", 41940), timeout=0.5)
                        s.sendall(b"quit\n")
                        s.close()
                        logger.info("vlc: sent 'quit' via RC socket.")
                    except Exception as e:
                        logger.warning(f"vlc rc quit failed: {e}")

                # short wait for graceful shutdown
                time.sleep(0.3)

                # ensure process is gone
                try:
                    self.process.kill()
                except Exception:
                    pass

        self.process = None
        logger.info(f"{self.__class__.__name__}.stop")
        return True
