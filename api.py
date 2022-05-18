from flask import Flask, jsonify
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
cors = CORS(app)

ROOT = "/"


@app.route('/contents', methods=['GET'])
def get_contents():
    input_path = ""
    path = Path(ROOT + input_path)
    if not path.exists():
        print(path)
        return jsonify({'message': f'Path {str(path)} does not exist.'})
    elif path.is_dir():
        return _get_dir_contents(path)
    elif path.is_file():
        return _get_file_contents(path)

    return jsonify({'message': 'There was an unknown error.'})


def _get_dir_contents(dir_path):
    results = {}
    for child in dir_path.iterdir():
        name = child.name + ("/" if child.is_dir else "")
        details = {
            'owner': child.owner(),
            'size': child.stat().st_size,
            'permissions': _format_file_permissions(child.stat().st_mode),
        }
        results[name] = details
    return jsonify({"contents": results})


def _format_file_permissions(mode_as_int):
    return oct(mode_as_int)[-3:]


def _get_file_contents(file_path):
    return jsonify({'contents': file_path.read_text()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
