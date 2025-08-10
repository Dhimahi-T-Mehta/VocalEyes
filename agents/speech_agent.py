"""
speech_agent.py
----------------
Agent 2: Speech Generation Agent

Responsibilities:
- Receive extracted text
- Convert text into natural speech
- Save MP3 locally
"""

import requests
from murf import Murf


class SpeechAgent:

    def __init__(self, api_key: str):
        self.client = Murf(api_key=api_key)

    def generate_speech(
        self,
        text: str,
        output_path: str = "output.mp3"
    ) -> str:

        response = self.client.text_to_speech.generate(

            text=text,

            voice_id="en-IN-rohan",

            style="Conversational",

            format="MP3",

            variation=3
        )

        if not response.audio_file:
            raise RuntimeError("Failed to generate speech.")

        audio = requests.get(response.audio_file)

        audio.raise_for_status()

        with open(output_path, "wb") as file:
            file.write(audio.content)

        return output_path