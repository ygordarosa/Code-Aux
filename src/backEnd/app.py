from flask import Flask, jsonify, request
from routes.get import getFolders
app = Flask(__name__)

@app.route("/get", methods=['GET'])
def hello_world():
    response = getFolders()
    return response



if __name__ == '__main__':
   app.run(port=3000)