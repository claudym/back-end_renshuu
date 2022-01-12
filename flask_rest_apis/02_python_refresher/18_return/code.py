def add(x, y):
  return x + y

result= add(5, 8)
print(result)

def divide(dividend, divisor):
  if divisor != 0:
    return dividend/divisor
  else:
    return "You fool!"

result= divide(15, 0)
print(result)

# Complete the function by making sure it returns 42. .
def return_42():
    # Complete function here
    # pass  # 'pass' just means "do nothing". Make sure to delete this!
    return 42

# Create a function below, called my_function, that takes two arguments and returns the result of its two arguments multiplied together.
def my_function(x, y):
  return x * y

print(return_42())
print(my_function(3, 6))