def named(**kwargs):
  print(kwargs)

named(name="Bobby", age=27)

def named(name, age):
  print(name, age)

details= {"name": "Bobby", "age": 27}
named(**details)

def named(**kwargs):
  print(kwargs)

def print_nicely(**kwargs):
  named(**kwargs)
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")

print_nicely(**{"name": "Bobby", "age": 27})
print_nicely(name="Bilxly Gene", age=29)

def both(*args, **kwargs):
  print(args)
  print(kwargs)

both(1, 2, 3, 4, name="el mejor", age=30)