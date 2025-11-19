import shlex
from enum import Enum, auto
import subprocess
import time

from bluer_objects.graphics.screen import get_size

from bluer_ugv.logger import logger


class VideoEngine(Enum):
    MPV = auto()
    VLC = auto()

    def pause(
        self,
        process: subprocess.Popen,
    ):
        try:
            # mpv understands "p" as toggle-pause.
            process.stdin.write(b"p")
            process.stdin.flush()
        except Exception as e:
            logger.error(f"failed to send pause command: {e}")
            return False

        return True

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

        if self == VideoEngine.MPV:
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

        if self == VideoEngine.VLC:
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
                    "--rc-host=127.0.0.1:41940",
                    shlex.quote(filename),
                ]
            )

        return "this-should-not-happen"

    def stop(
        self,
        process: subprocess.Popen,
    ):
        if self == VideoEngine.MPV:
            # MPV clean quit via stdin (if stdin was PIPE)
            try:
                if process.stdin:
                    process.stdin.write(b"q")
                    process.stdin.flush()
                else:
                    logger.info(f"{self.name.lower()}: no stdin; skipping quit.")
            except Exception as e:
                logger.warning(f"{self.name.lower()} quit failed: {e}")

        if self == VideoEngine.VLC:
            # VLC clean quit via TCP RC
            try:
                import socket

                s = socket.create_connection(("127.0.0.1", 41940), timeout=0.5)
                s.sendall(b"quit\n")
                s.close()
                logger.info("vlc: sent 'quit' via TCP RC.")
            except Exception as e:
                logger.warning(f"vlc rc quit failed: {e}")

        # Wait briefly for process to exit
        time.sleep(0.3)

        # Make sure it's gone
        try:
            process.kill()
        except Exception as e:
            logger.warning(f"process.kill failed: {e}")
