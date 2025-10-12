import random

class Robot:
    USED_NAMES = set()

    def _random_name(self):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        letter1 = random.choice(LETTERS)
        letter2 = random.choice(LETTERS)
        digit1 = random.randint(0, 9)
        digit2 = random.randint(0, 9)
        digit3 = random.randint(0, 9)

        digits_str = str(digit1) + str(digit2) + str(digit3)

        return letter1 + letter2 + digits_str

    def _unique_name(self):

        name = self._random_name()

        while name in Robot.USED_NAMES:
            name = self._random_name()

        Robot.USED_NAMES.add(name)
        return name

    def __init__(self):
        self.name = self._unique_name()

    def reset(self):
        Robot.USED_NAMES.discard(self.name)
        random.randint(0, 1)
        self.name = self._unique_name()