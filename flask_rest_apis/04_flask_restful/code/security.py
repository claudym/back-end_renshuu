from werkzeug.security import safe_str_cmp
from user import User

users= [
  User(1, "Bobby", "super_seguro_eh")
]

username_mapping= {u.username: u for u in users}
userid_mapping= {u.id: u for u in users}

#authenticate a user
def authenticate(username, password):
  user= username_mapping.get(username, None)
  # if user and user.password == password:
  if user and safe_str_cmp(user.password, password):
    return user

#identify a user
def identity(payload):
  user_id= payload["identity"]
  return userid_mapping.get(user_id, None)