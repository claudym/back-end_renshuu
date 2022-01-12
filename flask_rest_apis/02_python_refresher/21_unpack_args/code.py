# def multiply(*args):
#   print(args)
#   total= 1
#   for arg in args:
#     total *= arg
#   return total

# print(multiply(2, 3, 4))

# def add(x, y):
#   return x + y

# # nums = [3,5]
# # print(add(*nums))

# nums= {"x": 15, "y": 25}
# print(add(**nums))

def multiply(*args):
  total= 1
  for arg in args:
    total= total * arg
  
  return total

def apply(*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator provided to apply()."

print(apply(1, 3, 6, 7, operator="*"))