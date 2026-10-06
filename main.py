import time
from speech import SpeechInputModule
from config import MODEL


def main():
    si = SpeechInputModule(MODEL)

    while True:
        result = si.update()
        if result:
            print(result['text'])


if __name__ == "__main__":
    main()
