from flask import Flask,request

app = Flask(__name__)

@app.route('/edyoda')
def greet():
    return {"greet":"Hello Edyoda"}

app.run()