# Class for generating sound.
# Has some quality issues for performance.

import torch
from TTS.api import TTS
import hashlib

class Reader:
    def __init__(self, op_path = "static"):
        self.path = op_path
        self.tts = TTS(model_name="tts_models/ja/kokoro/tacotron2-DDC", progress_bar=False)


    # Generate a hash for the text based on the content
    # This is for caching (which is not implemented yet)
    def produce_sound(self, text):
        sha256_hash = hashlib.sha256(text.encode()).hexdigest()[:32]
        file_path=f"{self.path}/{sha256_hash}.wav"
        self.tts.tts_to_file(text, file_path=file_path)
        return file_path


