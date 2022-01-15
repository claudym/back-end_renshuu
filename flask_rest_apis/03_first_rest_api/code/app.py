from flask import Flask, jsonify, request

app= Flask(__name__) #__name__ is a special python variable: gives each file a unique name

stores= [
  {
    "name": "My amazing store",
    "items": [
      {
        "name": "another item",
        "price": 12.93
      }
    ]
  }
]

# @app.route("/")
# def home():
#   return "おはよう世界!"

# POST - used to receive data
# GET - used to send data back

# POST /store data: {name:}
@app.route("/store", methods=["POST"])
def create_store():
  request_data= request.get_json()
  store= {
    "name": request_data["name"],
    "items": []
  }
  stores.append(store)

  return jsonify(store)

# GET /store/<string:name>
@app.route("/store/<string:name>")
def get_store(name):
  for store in stores:
    if store["name"] == name:
      return jsonify(store)
  return jsonify({"message": "store not found TT"})

# GET /store
@app.route("/store")
def get_stores():
  return jsonify({"stores": stores})

# POST /store/<string:name>/item {name:, price:}
@app.route("/store/<string:name>/item", methods=["POST"])
def create_item_in_store(name):
  request_data= request.get_json()

  for store in stores:
    if store["name"] == name:
      item= {
        "name": request_data["name"],
        "price": request_data["price"]
      }
      store["items"].append(item)
      return jsonify(item)
  return jsonify({"message": "store not found TT"})


# GET /store/<string:name>/item
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
  for store in stores:
    if store["name"] == name:
      return jsonify({"items": store["items"]})
  return jsonify({"message": "store not found TT"})

app.run(port=5000)