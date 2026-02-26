import threading
import time

from bluer_options.env import BLUER_AI_CLOUD_IS_ACCESSIBLE
from bluer_objects.env import abcli_object_name
from bluer_agent.audio.properties import AudioProperties
from bluer_agent.audio.conversation import converse, greeting
from bluer_agent.rag.corpus.context import Context
from bluer_agent.env import BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT
from bluer_sbc.env import BLUER_SBC_AUDIO_ENABLED

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.config.classes import ClassicalConfig
from bluer_ugv.swallow.session.classical.leds import ClassicalLeds
from bluer_ugv.logger import logger


class ClassicalAudio:
    def __init__(
        self,
        config: ClassicalConfig,
        leds: ClassicalLeds,
    ):
        self.config = config
        self.leds = leds

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

        self.context = Context(
            BLUER_AGENT_RAG_CORPUS_SINGLE_ROOT_TEST_OBJECT,
            download=BLUER_AI_CLOUD_IS_ACCESSIBLE == 1,
        )

        self.running = False

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

    def loop(self):
        logger.info(f"{self.__class__.__name__}.loop started.")

        while self.running:
            if not self.config.get("audio_enabled"):
                time.sleep(0.01)
                continue

            converse(
                context=self.context,
                object_name=abcli_object_name,
                greeting=greeting,
                language=env.BLUER_UGV_AUDIO_LANGUAGE,
                audio_properties=self.audio_properties,
            )

            self.config.set("audio_enabled", False)
            time.sleep(0.01)
