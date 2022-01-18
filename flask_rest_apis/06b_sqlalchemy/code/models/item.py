import sqlite3

from helper.DBConnector import DBConnector

class ItemModel:
  def __init__(self, name, price):
    self.name= name
    self.price= price
  
  def json(self):
    return {"name": self.name, "price": self.price}
  
  @classmethod
  def find_by_name(cls, name):
    query= "SELECT name, price FROM items WHERE name=?"
    result= DBConnector.exec_query(query, (name,))
    return result