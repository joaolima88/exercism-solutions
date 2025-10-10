import random

class Robot:
    USED_NAMES = set()

    def random_name(self):
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return ''.join([random.choice(LETTERS), random.choice(LETTERS), str(random.randint(0, 9)),str(random.randint(0, 9)),str(random.randint(0, 9))])

    def unique_name(self):

        name = self.random_name()
        if name in Robot.USED_NAMES:
            name = self.unique_name()
        else:
            Robot.USED_NAMES.add(name)
            return name

    def __init__(self):
        self.name = self.unique_name()

    def reset(self):
        Robot.USED_NAMES.discard(self.name)
        random.randint(0, 1)
        self.name = self.unique_name()