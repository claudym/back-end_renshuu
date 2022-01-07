from flask import Flask, request
app = Flask(__name__)

#127.0.0.1:5000/
@app.route('/')
def hello_world():
  return "Hello 世界！"

@app.route('/hithere')
def hi_there_minna():
  return "/hithere hitto!"

@app.route('/bye')
def bye():
  #prepare a response for the request that came to /bye
  # joyo = "jouyou kanji yo"

  # tempJson={
  #   "field1":123
  # }

  # retJson= {
  #   "field1": 3,
  #   "field2": "def",
  #   "boolean": True,
  #   "array": [1,2,3,4,"abc"],
  #   "array of objects": [
  #     {
  #       "field1": 1
  #     },
  #     {
  #       "field2": "string yo!"
  #     }
  #   ],
  #   "array of nested arrays": [
  #     {
  #       "nested array": [
  #         {
  #           "field1": 1,
  #           "name": "kura"
  #         }
  #       ]
  #     }
  #   ]
  # }
  age = 2 * 14
  retJson = {
    "name": "kura",
    "age": age,
    "phones": [
      {
        "phoneName": "LG 200",
        "phoneNumber": 394725233,
        "wifi": False
      },
      {
        "phoneName": "iphone12",
        "phoneNumber": 44444,
        "wifi": True
      }
    ]
  }
  return retJson

@app.route("/add", methods=["POST"])
def add_two_nums():
  #get x,y from posted data
  dataDict = request.get_json()

  if "y" not in dataDict:
    return "ERROR", 305
  x= dataDict["x"]
  y= dataDict["y"]

  #add z=x+y
  z= x+y

  #prepare JSON, "z":z
  retJson = {
    "z": z
  }

  #return map_prepared
  return retJson

if __name__ == "__main__":
  # app.run(host="127.0.0.1", port=80)
  # app.run(debug=True)
  app.run(host="0.0.0.0", port=5000)