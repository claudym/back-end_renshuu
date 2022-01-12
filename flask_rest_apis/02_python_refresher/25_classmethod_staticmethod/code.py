# class ClassTest:
#   def instance_method(self):
#     print(f"Called instance_method of {self}")

#   @classmethod
#   def class_method(cls):
#     print(f"called class_method of {cls}")

#   @staticmethod
#   def static_method():
#     print("Called static_method.")


# test= ClassTest()
# test.instance_method()
# ClassTest().class_method()
# ClassTest().static_method()

# class Book:
#   TYPES= ("hardcover", "paperback")

#   def __init__(self, name, book_type, weight):
#     self.name= name
#     self.book_type= book_type
#     self.weight= weight
  
#   def __repr__(self):
#     return f'<Book "{self.name}", "{self.book_type}", weighing {self.weight}g>'
  
#   @classmethod
#   def hardcover(cls, name, page_weight):
#     return cls(name, cls.TYPES[0], page_weight + 100)
  
#   @classmethod
#   def paperback(cls, name, page_weight):
#     return cls(name, cls.TYPES[1], page_weight)

# # book= Book("Harry Potter and the Philosopher's Stone", "hardcover", 1500)
# book= Book.hardcover("Harry Potter and the Philosopher's Stone", 1500)
# libro= Book.paperback("The Left Hand of Darkness", 700)
# print(book)
# print(libro)


class Store:
  def __init__(self, name):
    self.name = name
    self.items = []

  def add_item(self, name, price):
    self.items.append({
        'name': name,
        'price': price
    })

  def stock_price(self):
    total = 0
    for item in self.items:
        total += item['price']
    return total

  @classmethod
  def franchise(cls, store):
    # Return another store, with the same name as the argument's name, plus " - franchise"
    return cls(store.name+" - franchise")

  @staticmethod
  def store_details(store):
    # Return a string representing the argument
    # It should be in the format 'NAME, total stock price: TOTAL'
    return f'{store.name}, total stock price: {store.stock_price()}'

honya= Store("Honya")
honya.add_item("Campus Notebook", 3)
honya.add_item("Butter", 4)
honya_f= Store.franchise(honya)
honya_f.add_item("Harry Potter", 5)
print(honya.name)
print(honya_f.name)
print(Store.store_details(honya))
print(Store.store_details(honya_f))
