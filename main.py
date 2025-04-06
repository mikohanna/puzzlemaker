from flask import Flask, jsonify
import tent_grid_generator as tents
import binairo_generator as binairo

app = Flask(__name__)

@app.route('/sample', methods=['GET'])
def generate_json():
    data = {"puzzle": [[1, 2, 3], [4, 5, 6]]}
    return jsonify(data)

@app.route('/tents_easy', methods=['GET'])
def generate_tents_easy():
    return jsonify(tents.generate_tents_grid(difficulty=1))


@app.route('/tents_medium', methods=['GET'])
def generate_tents_medium():
    return jsonify(tents.generate_tents_grid(difficulty=2))


@app.route('/tents_hard', methods=['GET'])
def generate_tents_hard():
    return jsonify(tents.generate_tents_grid(difficulty=3))


@app.route('/binairo_easy', methods=['GET'])
def generate_binairo_easy():
    return jsonify(binairo.generate_binairo_puzzle(difficulty=1))


@app.route('/binairo_medium', methods=['GET'])
def generate_binairo_medium():
    return jsonify(binairo.generate_binairo_puzzle(difficulty=2))


@app.route('/binairo_hard', methods=['GET'])
def generate_binairo_hard():
    return jsonify(binairo.generate_binairo_puzzle(difficulty=3))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
