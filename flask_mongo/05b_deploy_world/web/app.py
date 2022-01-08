from flask import Flask, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

server= Flask(__name__)
api= Api(server)

client= MongoClient("mongodb://db:27017")
db= client.SentencesDatabase
users= db["Users"]

class Register(Resource):
  def post(self):
    #step 1 - get posted data
    postedData= request.get_json()

    #get the data
    username= postedData["username"]
    password= postedData["password"]

    #hash(password+salt)= wgueytioufoiufcgety6u87635fhg2gi32v
    hashed_pw= bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    #store username and hashed_pw into database
    users.insert_one({
      "username": username,
      "password": hashed_pw,
      "sentence": "test sentence",
      "tokens": 5
    })

    retMap= {
      "status": 200,
      "msg": "You succesfully signed up for the API"
    }
    return retMap

def verifyPw(username, password):
  hashed_pw= users.find({
    "username": username
  })[0]["password"]

  if bcrypt.hashpw(password.encode(), hashed_pw) == hashed_pw:
    return True
  return False

def countTokens(username):
  tokens= users.find({
     "username": username
  })[0]["tokens"]
  return tokens

class Store(Resource):
  def post(self):
    postedData= request.get_json()

    username= postedData["username"]
    password= postedData["password"]
    sentence= postedData["sentence"]

    #verify username pw match
    correct_pw= verifyPw(username, password)
    if not correct_pw:
      retJson= {
        "status": 302,
        "message": "incorrect username/password"
      }
      return retJson
    
    #check if he has enough tokens
    num_tokens= countTokens(username)
    if num_tokens <= 0:
      retJson= {
        "status": 301,
        "message": "not enough tokens, gotta buy more idk how (it has to be implemented of course xD)"
      } 
      return retJson
    
    #store the sentence return 200 ok
    users.update_one({
      "username": username
    }, {
      "$set": {
        "sentence": sentence,
        "tokens": num_tokens-1
        }
    })
    retJson= {
      "status": 200,
      "message": "sentence saved successfully!"
    }
    return retJson

class Retrieve(Resource):
  def get(self):
    postedData= request.get_json()

    username= postedData["username"]
    password= postedData["password"]

    correct_pw= verifyPw(username, password)
    if not correct_pw:
      retJson= {
        "status": 302,
        "message": "incorrect username/password"
      }
      return retJson
    num_tokens= countTokens(username)
    if num_tokens <= 0:
      retJson= {
        "status": 301,
        "message": "not enough tokens, gotta buy more idk how (it has to be implemented of course xD)"
      }
      return retJson
    
    users.update_one({
      "username": username
    }, {
      "$set": {
        "tokens": num_tokens-1
      }
    })
    sentence= users.find({
      "username": username      
    })[0]["sentence"]
    retMap= {
      "status": 200,
      "message": {
        "sentence": sentence
      }
    }
    return retMap


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Retrieve, '/retrieve')

