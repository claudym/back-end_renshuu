def add(x, y):
  # pass  #do nothing (functions expects an indented block)
  result = x+y
  print(result)

add(5, 3)

def say_hello(name, surname):
  print(f"Hello {name} {surname}!")

say_hello("Tony", "Stank")
say_hello(surname="Toy", name="Story")

def divide(dividend, divisor):
  if divisor != 0:
    print(dividend/divisor)
  else:
    print("You fool!")

divide(13, divisor=0)
divide(13, 2)