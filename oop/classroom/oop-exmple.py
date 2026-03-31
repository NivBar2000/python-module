# student0 = {
#     "name": "Rolf",
#     "grades": (90, 90, 85, 88)
# }

# print(student0["name"])

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student0["grades"]))

# student.average()

class Student:
    def __init__(self, name, grades = (0, 0, 0, 0)):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student1 = Student("Rolf", (90, 90, 85, 88))
student2 = Student("Anna", (78, 82, 80, 79))
student3 = Student("Ben", (88, 91, 87, 90))
student4 = Student("Lila", (92, 89, 94, 91))

# print(student1.name)
# print(student1.grades)

print(student1.average())
print(student2.average())
print(student3.average())
print(student4.average())

# print(student2.name)
# print(student2.grades)

# print(student1)