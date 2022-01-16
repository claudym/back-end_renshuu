import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class DBConnector():
  def __init__(self, db_name):
    self.db_name= db_name

  def exec_query(self, query, val_tuple, commit=False):
    connection= sqlite3.connect(self.db_name)
    cursor= connection.cursor()
    try:
      result= cursor.execute(query, val_tuple)
    except Exception as err:
      connection.close()
      return err
    else:
      if commit:
        connection.commit()
      result= result.fetchall()
      connection.close()
      return result

class Item(Resource):
  db_connector= DBConnector("data.db")
  parser= reqparse.RequestParser()
  parser.add_argument("price",
    type=float,
    required=True,
    help="Required field"
  )

  @classmethod
  def find_by_name(cls, name):
    query= "SELECT name, price FROM items WHERE name=?"
    result= Item.db_connector.exec_query(query, (name,))
    return result

  @jwt_required()
  def get(self, name):
    item= self.find_by_name(name)
    if isinstance(item, Exception):
      return {"error": f"{type(e)}: {e}"}, 400
    if len(item) == 0:
      return {"message": f"No item named {name}"}, 404
    item= item[0]
    return {"item": {
        "name": item[0],
        "price": item[1]
      }
    }    
  
  def post(self, name):
    data= Item.parser.parse_args()
    query= "INSERT INTO items VALUES (?, ?)"
    item= {"name": name, "price": data["price"]}
    result= Item.db_connector.exec_query(query, (item["name"], item["price"]), commit=True)

    if isinstance(result, Exception):
      if isinstance(result, sqlite3.IntegrityError):
        return {"message": f"{name} already in items"}, 400
      return {"error": f"{type(e)}: {e}"}, 400
    return item, 201
  
  def delete(self, name):
    item= self.find_by_name(name)
    if isinstance(item, Exception):
      return {"error": f"{type(e)}: {e}"}, 400
    if len(item) == 0:
      return {"message": f"No item named {name}"}, 400
    
    query= "DELETE FROM items WHERE name=?"
    result= Item.db_connector.exec_query(query, (name,), commit=True)
    if isinstance(result, Exception):
      return {"error": f"{type(e)}: {e}"}, 400
    return {"message": "Item deleted."}
  
  def put(self, name):
    data= Item.parser.parse_args()
    query= "INSERT OR REPLACE INTO items VALUES (?, ?)"
    item= {"name": name, "price": data["price"]}
    result= Item.db_connector.exec_query(query, (item["name"], item["price"]), commit=True)
    if isinstance(result, Exception):
      return {"error": f"{type(e)}: {e}"}, 400
    return item

class ItemList(Resource):
  def get(self):
    db_connector= DBConnector("data.db")
    query= "SELECT name, price FROM items"
    item_list= db_connector.exec_query(query, ())

    if isinstance(item_list, Exception):
      return {"error": f"{type(e)}: {e}"}, 400
    retList= [{"name": item[0], "price": item[1]} for item in item_list]
    return {"items": retList}