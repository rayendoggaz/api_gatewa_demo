from flask import Flask, jsonify

app = Flask(__name__)

# Sample endpoint 1
@app.route('/api/resource1')
def get_resource1():
    return jsonify({'data': 'This is Resource 1'})

# Sample endpoint 2
@app.route('/api/resource2')
def get_resource2():
    return jsonify({'data': 'This is Resource 2'})

if __name__ == '__main__':
    app.run(debug=True)
