class Character:
    def __init__(self):
        import random
        self.strength = sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])
        self.dexterity = sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])
        self.constitution = sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])
        self.intelligence = sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])
        self.wisdom = sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])
        self.charisma = sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        import random
        idx = random.randint(1,6)
        return [self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma][idx]


def modifier(value):
    return (value - 10) // 2