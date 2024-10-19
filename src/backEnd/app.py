from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/get", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == '__main__':
   app.run(port=3000)