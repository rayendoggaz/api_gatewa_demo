from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# API Gateway routing
@app.route('/api/<path:path>', methods=['GET'])
def api_gateway(path):
    # Define endpoint mappings
    endpoint_mappings = {
        'resource1': 'http://localhost:5000/api/resource1',
        'resource2': 'http://localhost:5000/api/resource2'
    }

    # Get the corresponding endpoint URL
    endpoint_url = endpoint_mappings.get(path)
    if endpoint_url:
        # Forward the request to the appropriate endpoint
        response = requests.get(endpoint_url)
        return response.json(), response.status_code
    else:
        return jsonify({'error': 'Endpoint not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=8090)
