import random

def random_name():
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        letter1 = random.choice(LETTERS)
        letter2 = random.choice(LETTERS)
        digit1 = random.randint(0, 9)
        digit2 = random.randint(0, 9)
        digit3 = random.randint(0, 9)

        digits_str = str(digit1) + str(digit2) + str(digit3)

        return letter1 + letter2 + digits_str

def unique_name(USED_NAMES):

        name = random_name()

        while name in USED_NAMES:
            name = random_name()

        USED_NAMES.add(name)
        return name

class Robot:
    USED_NAMES = set()
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self):
        self.name = unique_name(Robot.USED_NAMES)

    def reset(self):
        Robot.USED_NAMES.discard(self.name)
        random.randint(0, 1)
        self.name = unique_name(Robot.USED_NAMES)