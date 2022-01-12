from operator import itemgetter
# def divide(dividend, divisor):
#   if divisor == 0:
#     raise ZeroDivisionError("Division cannot be 0.")
  
#   return dividend / divisor

# def calculate(*values, operator):
#   return operator(*values)

# result= calculate(20, 4, operator=divide)
# print(result)

def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
  raise RuntimeError(f"Could not find an element with {expected}.")

friends= [
  {"name": "Rodolfo Smith", "age": 24},
  {"name": "Adam Wool", "age": 32},
  {"name": "Annie Villa", "age": 27}
]

# def get_friend_name(friend):
#   return friend["name"]
# print(search(friends, "Rodolfo Smith", get_friend_name))

# print(search(friends, "Rodolfo Smith", lambda friend: friend["name"]))
print(search(friends, "Rodolfo Smith", itemgetter("name")))