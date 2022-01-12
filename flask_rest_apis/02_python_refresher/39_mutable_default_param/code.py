from typing import List, Optional

class Student:
  # def __init__(self, name: str, grades: List[int] = []): # bad!!
  def __init__(self, name: str, grades: Optional[List[int]] = None): # bad!!
    self.name= name
    self.grades= grades or []
  
  def take_exam(self, result: int):
    self.grades.append(result)

bobby= Student("Bobby")
rodolfo= Student("Rodolfo")
bobby.take_exam(90)
print(bobby.grades)
print(rodolfo.grades)