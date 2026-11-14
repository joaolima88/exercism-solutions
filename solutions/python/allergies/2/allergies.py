class Allergies:

    def __init__(self, score):
        self.score = score
        self.items = {"eggs": 1, "peanuts": 2, "shellfish": 4, "strawberries": 8, "tomatoes": 16,
        "chocolate": 32, "pollen": 64, "cats": 128}
    
        
    def allergic_to(self, item):
        return bool(self.score & self.items[item])

    @property
    def lst(self):
        alergens = []
        for i in self.items:
            if self.allergic_to(i):
                alergens.append(i)
        return alergens