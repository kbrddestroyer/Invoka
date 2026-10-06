import json
from vosk import Model, KaldiRecognizer

from config import RATE
from micro import MicrophoneInput


class SpeechInputModule:
    def __init__(self, model_path: str):
        self._recogniser = KaldiRecognizer(Model(model_path), RATE)
        self._input = MicrophoneInput()
        self._input.open()

    def start(self):
        pass

    def update(self):
        data = self._input.read()

        if not self._recogniser.AcceptWaveform(data):
            return None

        result = json.loads(self._recogniser.Result())
        return result
