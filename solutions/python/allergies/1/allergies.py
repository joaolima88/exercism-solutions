class Allergies:

    def __init__(self, score):
        self.score = score
        self.d = {  1:'eggs',
                    2: 'peanuts',
                    4: 'shellfish',
                    8: 'strawberries',
                    16: 'tomatoes',
                    32: 'chocolate',
                    64: 'pollen',
                    128: 'cats'}

    @property
    def lst(self):
        x = self.score
        l= []

        if x%2 != 0:
            x -= 1
            l.append(1)

        exp = 1

        while 2**exp <= x:
            exp += 1

        exp -= 1

        while exp > 0 and x > 0:
            current = 2**exp
            if x - current < 0:
                exp -= 1
            else:
                x = x - current
                exp -= 1
                l.append(current)

        l = sorted(l,reverse=True)

        while sum(l) > 256:
            l.pop(0)

        allergies = []
        for i in l:
            allergies.append(self.d[i])
            

        return allergies[::-1]
    

    
    def allergic_to(self, item):
        if item in Allergies(self.score).lst:
            return True
        else:
            return False