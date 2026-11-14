class Garden:
    def __init__(self, diagram, students=["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]):
        self.diagram = diagram.split()
        self.students = sorted(students)

    def plants(self, name):

        plants={'G':'Grass', 'C':'Clover', 'R': "Radishes", 'V': "Violets"}

        ind = self.students.index(name) * 2
        row1_plants = plants[self.diagram[0][ind]], plants[self.diagram[0][ind+1]]
        row2_plants = plants[self.diagram[1][ind]], plants[self.diagram[1][ind+1]]
        [*f] = *row1_plants, *row2_plants
        return f
        