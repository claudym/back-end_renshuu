import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel
from helper.DBConnector import DBConnector

class Item(Resource):
  parser= reqparse.RequestParser()
  parser.add_argument("price",
    type=float,
    required=True,
    help="Required field"
  )

  # @jwt_required()
  def get(self, name):
    item= ItemModel.find_by_name(name)
    if isinstance(item, Exception):
      return {"error": f"{type(e)}: {e}"}, 500
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
    result= DBConnector.exec_query(query, (item["name"], item["price"]), commit=True)

    if isinstance(result, Exception):
      if isinstance(result, sqlite3.IntegrityError):
        return {"message": f"{name} already in items"}, 400
      return {"error": f"{type(e)}: {e}"}, 500
    return item, 201
  
  def delete(self, name):
    item= ItemModel.find_by_name(name)
    if isinstance(item, Exception):
      return {"error": f"{type(e)}: {e}"}, 500
    if len(item) == 0:
      return {"message": f"No item named {name}"}, 400
    
    query= "DELETE FROM items WHERE name=?"
    result= DBConnector.exec_query(query, (name,), commit=True)
    if isinstance(result, Exception):
      return {"error": f"{type(e)}: {e}"}, 500
    return {"message": "Item deleted."}
  
  def put(self, name):
    data= Item.parser.parse_args()
    query= "INSERT OR REPLACE INTO items VALUES (?, ?)"
    item= {"name": name, "price": data["price"]}
    result= DBConnector.exec_query(query, (item["name"], item["price"]), commit=True)
    if isinstance(result, Exception):
      return {"error": f"{type(e)}: {e}"}, 500
    return item


class ItemList(Resource):
  def get(self):
    query= "SELECT name, price FROM items"
    item_list= DBConnector.exec_query(query, ())

    if isinstance(item_list, Exception):
      return {"error": f"{type(e)}: {e}"}, 500
    retList= [{"name": item[0], "price": item[1]} for item in item_list]
    return {"items": retList}