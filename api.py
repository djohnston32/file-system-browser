from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET'])
def get_stores():
    return jsonify({'contents': 'hello world'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
