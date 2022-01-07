from flask import Flask, request
from flask_restful import Api, Resource

server = Flask(__name__)
api = Api(server)

@server.route('/')
def hello_world():
  return "Hello 世界！"

@server.route('/hithere')
def hi_there_minna():
  return "/hithere hitto!"

def checkPostedData(postedData, functionName):
  if functionName in ["add", "subtract", "multiply"]:
    if "x" not in postedData or "y" not in postedData:
      return 301
    elif not isinstance(postedData["x"], int) or not isinstance(postedData["y"], int):
      return 302
    else:
      return 200
  elif functionName == "divide":
    if "x" not in postedData or "y" not in postedData:
      return 301
    elif not isinstance(postedData["x"], int) or not isinstance(postedData["y"], int):
      return 302
    elif postedData["y"] == 0:
      return 303
    else:
      return 200

class Add(Resource):
  def post(self):
    postedData = request.get_json()

    # verify postedData
    status_code = checkPostedData(postedData, "add")
    if status_code != 200:
      retJson = {
        "message": "Error!",
        "status code": status_code
      }
      return retJson

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)
    ret= x+y
    retMap = {
      "message": ret,
      "status code": 200
    }

    return retMap

class Subtract(Resource):
  def post(self):
    postedData = request.get_json()

    # verify postedData
    status_code = checkPostedData(postedData, "subtract")
    if status_code != 200:
      retJson = {
        "message": "Error!",
        "status code": status_code
      }
      return retJson

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)
    ret= x-y
    retMap = {
      "message": ret,
      "status code": 200
    }

    return retMap

class Multiply(Resource):
  def post(self):
    postedData = request.get_json()

    # verify postedData
    status_code = checkPostedData(postedData, "multiply")
    if status_code != 200:
      retJson = {
        "message": "Error!",
        "status code": status_code
      }
      return retJson

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)
    ret= x*y
    retMap = {
      "message": ret,
      "status code": 200
    }

    return retMap

class Divide(Resource):
  def post(self):
    postedData = request.get_json()

    # verify postedData
    status_code = checkPostedData(postedData, "divide")
    if status_code != 200:
      retJson = {
        "message": "Error!",
        "status code": status_code
      }
      return retJson

    x = postedData["x"]
    y = postedData["y"]
    x = int(x)
    y = int(y)
    ret= x/y
    retMap = {
      "message": ret,
      "status code": 200
    }

    return retMap

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")

# @server.route("/")
# def hello():
#   return "hola"