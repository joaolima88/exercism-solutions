class School:

    def __init__(self, r=None, a=None):
        self.r = {}
        self.a = []

    def add_student(self, name, grade):
        if name in self.r.keys():
            self.a.append(False)
        else:
            self.r[name] = grade
            self.a.append(True)


    def roster(self):
        return [i[0] for i in sorted(self.r.items(), key=lambda i: (i[1], i[0]))]

    def grade(self, grade_number):
        return sorted([i for i in self.r.keys() if self.r[i] == grade_number])

    def added(self):
        return self.a