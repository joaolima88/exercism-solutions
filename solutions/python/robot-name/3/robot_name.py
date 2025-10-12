import random

class Robot:
    USED_NAMES = set()

    def _random_name(self):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join([random.choice(LETTERS), random.choice(LETTERS), str(random.randint(0, 9)),str(random.randint(0, 9)),str(random.randint(0, 9))])

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