from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    response = {
        'greeting': 'Hello, World!'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)