# class Person:
#   def __init__(self, name, age):
#     self.name= name
#     self.age= age
#   def __str__(self):
#     return f"Person {self.name}, {self.age} years old."
#   def __repr__(self):
#     return f"<Person('{self.name}', {self.age})>"

# bobby= Person("Bobby", 24)
# print(bobby)
# print(bobby.__repr__())


class Store:
  def __init__(self, name):
    # You'll need 'name' as an argument to this method.
    # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    self.name= name
    self.items= []

  def add_item(self, name, price):
    # Create a dictionary with keys name and price, and append that to self.items.
    self.items.append({"name": name, "price": price})

  def stock_price(self):
    # Add together all item prices in self.items and return the total.
    # total= sum([x["price"] for x in self.items])      #with list comprehension
    total= sum(map(lambda item: item["price"], self.items))   #with lambda function and map
    return total

honya= Store("Honya")
honya.add_item("Campus Notebook", 3)
honya.add_item("Butter", 4)
honya.add_item("Box", 1)
print(honya.stock_price())