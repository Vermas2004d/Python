#creating a basic python server with flask and python


#Flask is used to make the websites and the api's

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/secret")
def secret_page():
    return "<h1>You are in the Secret Page</h1>"

app.run()