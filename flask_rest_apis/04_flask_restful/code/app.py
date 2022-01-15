from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity  

app= Flask(__name__)
app.secret_key= "lesecretKey"
api= Api(app)

jwt= JWT(app, authenticate, identity) # /auth

items= []
items_set= set()

class Item(Resource):
  parser= reqparse.RequestParser()
  parser.add_argument("price",
    type=float,
    required=True,
    help="Required field"
  )

  @jwt_required()
  def get(self, name): 
    if name not in items_set:
      return {"message": f"No items named {name}"}, 404
    
    item= next(filter(lambda item: item["name"] == name, items))
    return {"item": item}

  def post(self, name):
    if name in items_set:
      return {"message": f"{name} already in Items"}, 400
    
    data= Item.parser.parse_args()
    item= {"name": name, "price": data["price"]}
    items_set.add(name)
    items.append(item)
    return item, 201
  
  def delete(self, name):
    if name not in items_set:
      return {"message": f"No item named {name}"}, 400
    
    global items
    items= list(filter(lambda elem: elem["name"] != name, items))
    items_set.remove(name)
    return {"message": "Item deleted."}
  
  def put(self, name):
    # data= request.get_json()
    data= Item.parser.parse_args()
    item= {"name": name, "price": data["price"]}

    if name in items_set:
      # for i in range(len(items)):
      #   if items[i]["name"] == name:
      #     items[i].update(data)
      #     break    
      next(filter(lambda x: x["name"] == name, items)).update(data)
    else:    
      items_set.add(name)
      items.append(item)
    return item

class Items(Resource):
  def get(self):
    return {"items": items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items")


app.run(port=5000, debug=True)