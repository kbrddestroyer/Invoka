import time
from source.speech import SpeechInputModule
from source.config import MODEL
from source.keyboard_controller import Cast


def main():
    si = SpeechInputModule(MODEL)

    while True:
        result = si.update()
        if not result:
            continue

        voice_prompt = result['text']
        print(voice_prompt)
        for prompt in voice_prompt.split(' '):
            Cast.invoke_spell(prompt)


if __name__ == "__main__":
    main()
