from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return str(random.randint(1, 100))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
