from flask import Flask, jsonify
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
cors = CORS(app)

ROOT = ""


@app.route('/contents/', defaults={'input_path': '/'}, methods=['GET'])
@app.route('/contents/<path:input_path>', methods=['GET'])
def get_contents(input_path):
    try:
        path = Path(ROOT + input_path)
    except:
        return {'message': 'Invalid input path.'}, 400

    if not path.exists():
        return jsonify({'message': f'Path {str(path)} does not exist.'}), 404
    elif path.is_dir():
        return _get_dir_contents(path)
    elif path.is_file():
        return _get_file_contents(path)

    return jsonify({'message': 'The path was of an unknown type.'}), 500


def _get_dir_contents(dir_path):
    results = {}
    for child in dir_path.iterdir():
        name = child.name + ("/" if child.is_dir() else "")
        details = {
            'owner': child.owner(),
            'size': child.stat().st_size,
            'permissions': _format_file_permissions(child.stat().st_mode),
        }
        results[name] = details
    return jsonify({"contents": results}), 200


def _format_file_permissions(mode_as_int):
    return oct(mode_as_int)[-3:]


def _get_file_contents(file_path):
    return jsonify({'contents': file_path.read_text()}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
