from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required



from security import authenticate, identity  

app= Flask(__name__)
app.secret_key= "lesecretKey"
api= Api(app)

jwt= JWT(app, authenticate, identity) # /auth

items= []
items_set= set()

class Item(Resource):
  @jwt_required()
  def get(self, name):
    if name in items_set:
      item= next(filter(lambda item: item["name"] == name, items))
      return {"item": item}
    return {"message": f"No items named {name}"}, 404

  def post(self, name):
    data= request.get_json()
    item= {"name": name, "price": data["price"]}

    if name not in items_set:
      items_set.add(name)
      items.append(item)
      return item, 201
    return {"message": f"{name} already in Items"}, 400

class Items(Resource):
  def get(self):
    return {"items": items}

api.add_resource(Item, "/item/<string:name>")
api.add_resource(Items, "/items")


app.run(port=5000, debug=True)