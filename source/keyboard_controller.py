import time
import random
import keyboard

from keybinds import Keys


class Cast:
    DELAY_MIN = 0.05
    DELAY_MAX = 0.2

    def __init__(self, keys: list, aliases: str):
        self._aliases = aliases.strip().lower()
        self._keys = ""
        for key in keys:
            self._keys += Keys.KEYBINDS[key]

    def _apply_key(self, ch):
        keyboard.write(ch)
        print (ch)
        time.sleep(random.uniform(self.DELAY_MIN, self.DELAY_MAX))

    def invoke(self):
        for ch in self._keys:
            self._apply_key(ch)

    def check(self, prompt: str):
        return prompt in self._aliases and len(prompt) > 2

    @staticmethod
    def invoke_spell(voice_input: str):
        global SPELLS

        # 1. normalize
        voice_input = voice_input.strip().lower().replace(' ', '')
        if 'the' == voice_input[:3]:
            voice_input = voice_input[3:]

        # Well, not that optimal
        for spell in SPELLS:
            if not spell.check(voice_input):
                continue

            spell.invoke()
            return


SPELLS = [
    Cast([Keys.QUAS], "quas, first, one"),
    Cast([Keys.WEX], "wex, second, two"),
    Cast([Keys.EXORT], "exort, third, three"),
    Cast([Keys.ULTIMATE], "ultimate, ulti, ult, invoke"),
    Cast([Keys.WEX, Keys.WEX, Keys.WEX, Keys.ULTIMATE, Keys.ALT1], "emp"),
    Cast([Keys.QUAS, Keys.WEX, Keys.WEX, Keys.ULTIMATE, Keys.ALT1], "tornado"),
    Cast([Keys.EXORT, Keys.EXORT, Keys.EXORT, Keys.ULTIMATE, Keys.ALT1], "sunstrike"),
]