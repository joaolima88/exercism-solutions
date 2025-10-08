class Character:
    def __init__(self):
        self.strength = random()
        self.dexterity = random()
        self.constitution = random()
        self.intelligence = random()
        self.wisdom = random()
        self.charisma = random()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        import random
        return [self.strength,self.dexterity,self.constitution,self.intelligence,self.wisdom,self.charisma][random.randint(1,6)]


def modifier(value):
    return (value - 10) // 2

def random():
    import random
    return sum(sorted([random.randint(1,6),random.randint(1,6),random.randint(1,6),random.randint(1,6)])[1:])