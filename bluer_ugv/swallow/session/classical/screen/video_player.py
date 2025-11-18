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
                "dryrun mode" if dryrun else "",
            )
        )

    def pause(self) -> bool:
        if not self.dryrun:
            if self.process and self.process.poll() is None:
                try:
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
    ) -> bool:
        if not file.exists(filename):
            logger.error(f"file not found: {filename}")
            return

        if not self.dryrun:
            # start omxplayer fullscreen.
            loop_flag = "--loop" if loop else ""
            cmd = f"omxplayer -b {loop_flag} {shlex.quote(filename)}"
            logger.info(f"running: {cmd}")

            # Kill previous playback if running
            self.stop()

            try:
                self.process = subprocess.Popen(
                    shlex.split(cmd),
                    stdin=subprocess.PIPE,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            except Exception as e:
                logger.error(f"failed to run omxplayer: {e}")
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
                    self.process.stdin.write(b"q")
                    self.process.stdin.flush()
                except Exception as e:
                    logger.warning(e)
                    pass

                time.sleep(0.3)
                self.process.kill()

        self.process = None

        logger.info(f"{self.__class__.__name__}.stop")
        return True
