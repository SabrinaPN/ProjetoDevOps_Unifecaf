from flask import Flask, jsonify, request
import os
import uuid

app = Flask(__name__)
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')

@app.get('/health')
def health():
    return jsonify(status='ok', service='payments', version=APP_VERSION), 200

@app.get('/ready')
def ready():
    return jsonify(status='ready', service='payments'), 200

@app.post('/charge')
def charge():
    payload = request.get_json(force=True)
    amount = float(payload.get('amount', 0))
    return jsonify(status='AUTHORIZED', transaction_id=str(uuid.uuid4()), amount=amount), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)
