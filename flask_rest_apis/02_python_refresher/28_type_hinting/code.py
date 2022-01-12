from typing import List

def list_avg(sequence: List) -> float:
  return sum(sequence)/len(sequence)

print(list_avg([1,2,3]))