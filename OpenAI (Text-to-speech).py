# -*- coding: utf-8 -*-


pip install openai;

from pathlib import Path
from openai import OpenAI
client = OpenAI(
    api_key = "your-key"
)

speech_file_path = "path/speech.mp3"
response = client.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input="Today is a wonderful day to build something people love!"
)

response.stream_to_file(speech_file_path)
