from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate_json():
    # Example JSON data
    data = {"puzzle": [[1, 2, 3], [4, 5, 6]]}
    
    return jsonify(data)  # Sends JSON response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
