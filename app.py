from flask import Flask, jsonify, request
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return "Server created successfully!"

@app.route('/hash', methods=['POST'])
def hash():
    str = request.json['data']
    s = hashlib.sha256()
    s.update(str.encode('utf-8'))
    return jsonify({'hash' : s.hexdigest()}) 

if __name__ == '__main__':
    app.run(debug=True, port=8787)