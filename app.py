from flask import Flask, jsonify, request, Response
import requests

app = Flask(__name__)


SERVER_A_BASE_URL = 'http://localhost:3000'

@app.route('/<format>')
def forward_to_server_a(format):
    """
    Forwards the request to Server A and returns its response.
    """
    response = requests.get(f'{SERVER_A_BASE_URL}/{format}')
    
   
    return Response(response.content, mimetype=response.headers['Content-Type'])

if __name__ == '__main__':
    app.run(debug=True, port=5001)
