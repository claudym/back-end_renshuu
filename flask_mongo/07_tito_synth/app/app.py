from flask import Flask, render_template
server = Flask(__name__)

@server.route('/')
def synthesis():
  # WEB pages
  return render_template("index.html")
