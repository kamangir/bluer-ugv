from typing import List, Optional
import subprocess
import shlex
import time

from bluer_options.logger.config import log_list
from bluer_objects import file

from bluer_ugv.logger import logger


class VideoPlayer:
    def __init__(
        self,
        dryrun: bool = False,
    ):
        self.process: Optional[subprocess.Popen] = None
        self.current_file: Optional[str] = None

        self.paused = False
        self.dryrun = dryrun

        logger.info(
            "{} created{}.".format(
                self.__class__.__name__,
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
    ) -> bool:
        if not file.exists(filename):
            logger.error(f"file not found: {filename}")
            return False

        if not self.dryrun:
            cmd = " ".join(
                [
                    "mpv",
                    "--fs",  # request fullscreen
                    "--x11-bypass-compositor=yes",  # CRITICAL for LXDE on Pi
                    "--no-border",  # remove decorations
                    "--geometry=0:0",  # position at 0,0
                    "--ontop",  # stay above desktop panels
                    "--keepaspect=yes",  # preserve aspect ratio
                    "--no-keepaspect-window",  # add black bars if needed
                    "--loop" if loop else "",
                    "--no-audio" if not audio else "",
                    shlex.quote(filename),
                ]
            )
            logger.info(f"running: {cmd}")

            # Kill previous playback if running
            self.stop()

            try:
                # pylint: disable=consider-using-with
                self.process = subprocess.Popen(
                    shlex.split(cmd),
                    stdin=subprocess.PIPE,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except Exception as e:
                logger.error(f"failed to run mpv: {e}")
                self.process = None
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
                try:
                    # mpv: quit = "q"
                    self.process.stdin.write(b"q")
                    self.process.stdin.flush()
                except Exception as e:
                    logger.warning(e)

                time.sleep(0.3)
                self.process.kill()

        self.process = None

        logger.info(f"{self.__class__.__name__}.stop")
        return True
