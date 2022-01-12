def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("You fool TT")
  return dividend/divisor

students = [
  {"name": "Bobby", "grades": [75, 90]},
  {"name": "Rodolfo", "grades": [50]},
  {"name": "Jenny", "grades": [100, 90]}
]

try:
  for student in students:
    name= student["name"]
    grades= student["grades"]
    average= divide(sum(grades), len(grades))
    print(f"{name} averaged {average:.2f}.")
except ZeroDivisionError as e:
  print(f"ERROR: {name} has no grades!")
else:
  print("All student average calculated!!!")
finally:
  print("ありがとう！")
