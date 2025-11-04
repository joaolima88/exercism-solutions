class School:

    def __init__(self, r=None, a=None):
        self.r = r if r is not None else []
        self.a = a if a is not None else []

    def add_student(self, name, grade):
        if name  in [i[1] for i in self.r]:
            self.a.append(False)
        else:
            self.r.append((grade, name))
            self.a.append(True)

    def roster(self):
        self.r = sorted(self.r)
        return [i[1] for i in self.r]

    def grade(self, grade_number):
        return sorted([i[1] for i in self.r if i[0] == grade_number])
        
    def added(self):
        return self.a