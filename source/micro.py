import pyaudio

from config import RATE


class MicrophoneInput:
    def __init__(self):
        self._mic = pyaudio.PyAudio()
        self._stream = None

    def open(self):
        self._stream = self._mic.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=RATE,
            input=True,
            frames_per_buffer=4000
        )

        self._stream.start_stream()

    def read(self):
        data = self._stream.read(4096, exception_on_overflow=False)
        return data

    def finalize(self):
        self._stream.stop_stream()
        self._stream.close()
        self._mic.terminate()

    def __del__(self):
        self.finalize()
