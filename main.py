from flask import Flask, jsonify
import tent_grid_generator as tents

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_json():
    # Example JSON data
    data = {"puzzle": [[1, 2, 3], [4, 5, 6]]}
    
    return jsonify(data)  # Sends JSON response

@app.route('/tents_easy', methods=['GET'])
def generate_tents_easy():
    # Example JSON data
    data = tents.generate_tents_grid(difficulty=1)
    
    return jsonify(data)  # Sends JSON response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
