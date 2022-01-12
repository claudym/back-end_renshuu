class Student:
  def __init__(self, name, grades):
    self.name= name
    self.grades= grades

  def average(self):
    return sum(self.grades)/len(self.grades)

student= Student("Bob", (73, 83, 93, 80, 90))
print(student.name)
print(student.grades)
print(student.average())
