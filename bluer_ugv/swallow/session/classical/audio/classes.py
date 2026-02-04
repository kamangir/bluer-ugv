import threading
import time
from typing import Dict, List

from bluer_objects.env import abcli_object_name
from bluer_objects.metadata import post_to_object
from bluer_agent.audio.play import play
from bluer_agent.audio.properties import AudioProperties
from bluer_agent.chat.functions import chat
from bluer_agent.rag.corpus.context import Context
from bluer_agent.rag.prompt import build_prompt
from bluer_agent.transcription.functions import transcribe
from bluer_agent.voice.functions import generate_voice
from bluer_agent.env import BLUER_AGENT_RAG_CORPUS_TEST_OBJECT
from bluer_sbc.env import BLUER_SBC_AUDIO_ENABLED

from bluer_ugv import env
from bluer_ugv.swallow.session.classical.config import ClassicalConfig
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
            BLUER_AGENT_RAG_CORPUS_TEST_OBJECT,
            download=True,
        )

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

        audio_prompt: str = "سلام، من رنگین هستم. چطور می‌تونم کمک‌تون کنم؟"
        while self.running:
            if not self.config.get("audio_enabled"):
                time.sleep(0.01)
                continue

            success, filename = generate_voice(
                object_name=abcli_object_name,
                sentence=audio_prompt,
            )
            if not success:
                time.sleep(1)
                continue

            self.leds.flash("yellow")

            play(
                object_name=abcli_object_name,
                filename=filename,
            )

            self.leds.flash("red")
            time.sleep(1)

            success, query = transcribe(
                object_name=abcli_object_name,
                language=env.BLUER_UGV_AUDIO_LANGUAGE,
                record=True,
                properties=self.audio_properties,
            )
            if not success or not query:
                if not query:
                    self.config.set("audio_enabled", False)

                time.sleep(1)
                continue

            self.leds.flash("yellow")

            success, query_context = self.context.generate(
                query=query,
            )
            if not success:
                time.sleep(1)
                continue

            success, reply = chat(
                messages=build_prompt(
                    query=query,
                    context=query_context["chunks"],
                )
            )
            if not success:
                time.sleep(1)
                continue

            self.leds.flash("yellow")

            success, reply_sentence = self.context.understand_reply(reply)
            if not success:
                time.sleep(1)
                continue

            self.log += [
                {
                    "user": query,
                    "assistant": reply_sentence,
                },
            ]

            audio_prompt = reply_sentence
