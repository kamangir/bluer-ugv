import threading
import time
from typing import Dict, List

from bluer_objects.env import abcli_object_name
from bluer_objects.metadata import post_to_object

from bluer_agent.audio.properties import AudioProperties
from bluer_agent.transcription.functions import transcribe
from bluer_sbc.env import BLUER_SBC_AUDIO_ENABLED

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.logger import logger


class ClassicalAudio:
    def __init__(
        self,
        leds: ClassicalLeds,
    ):
        self.enabled = BLUER_SBC_AUDIO_ENABLED == 1
        logger.info(
            "{}: {}".format(
                self.__class__.__name__,
                ("enabled" if self.enabled else "disabled"),
            )
        )

        self.audio_properties = AudioProperties(
            rate=env.BLUER_UGV_AUDIO_RATE,
            channels=env.BLUER_UGV_AUDIO_CHANNELS,
            length=env.BLUER_UGV_AUDIO_LENGTH,
        )

        self.leds = leds

        self.running = False

        self.log: List[Dict[str, Dict]] = []

        if not self.enabled:
            return

        self.running = True
        self.thread = threading.Thread(target=self.loop, daemon=True)
        self.thread.start()

    def stop(self):
        if not self.enabled:
            return

        self.running = False
        self.thread.join()

        logger.info(f"{self.__class__.__name__}.stopped.")

        post_to_object(
            abcli_object_name,
            "audio",
            self.log,
        )

    def loop(self):
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            success, text = transcribe(
                object_name=abcli_object_name,
                language=env.BLUER_UGV_AUDIO_LANGUAGE,
                record=True,
                properties=self.audio_properties,
            )
            if success:
                self.leds.flash("red")
                self.log += [
                    {"user": text},
                ]

            time.sleep(1)
