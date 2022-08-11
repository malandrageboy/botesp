import flask
from flask import Flask, escape, request, jsonify, make_response
import json
from time import sleep
from flask_cors import CORS

app = Flask(__name__)

saved_message = ""

@app.route('/', methods=['GET'])
def home():
    return jsonify({"Hello": "v bot"})

@app.route("/message", methods=['GET', 'POST'])
def message():
    global saved_message
    
    if request.method == "POST":
        content = request.json
        saved_message = content['message']
        
        print("Message saved: " + saved_message)
        return jsonify({"Message Sended": saved_message}), 200


    if request.method == 'GET':
        return jsonify({"message": saved_message}), 200

if __name__ == "__main__":
    app.run(debug=False, host= '0.0.0.0')
