def add(x, y):
  return x + y
add = lambda x, y: x + y
print(add(5, 7))

print((lambda x, y: x + y)(5,7)) #not very com

def double (x):
  return x * 2

sequence= [1, 3, 5, 9]
doubled= [double(x) for x in sequence]
print(doubled)
doubled= list(map(double, sequence))
print(doubled)
doubled= [(lambda x: x * 2)(x) for x in sequence] #with lambda; convoluted
print(doubled)
doubled= list(map(lambda x: x * 2, sequence)) #used this preferrably (inside map, reduced, etc)

print(doubled)