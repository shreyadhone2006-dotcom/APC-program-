class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, name, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)
        self.name = name

    def performance(self):
        total = self.marks + self.points
        print("Name:", self.name)
        print("Academic Marks:", self.marks)
        print("Sports Points:", self.points)
        print("Overall Performance:", total)


s = Student("Priya", 85, 10)
s.performance()