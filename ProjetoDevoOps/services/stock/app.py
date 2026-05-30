from flask import Flask, jsonify, request
import os

app = Flask(__name__)
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')
INVENTORY = {'SKU-001': 100, 'SKU-002': 50, 'SKU-003': 25}

@app.get('/health')
def health():
    return jsonify(status='ok', service='stock', version=APP_VERSION), 200

@app.get('/ready')
def ready():
    return jsonify(status='ready', service='stock'), 200

@app.post('/reserve')
def reserve():
    payload = request.get_json(force=True)
    sku = payload.get('sku', 'SKU-001')
    quantity = int(payload.get('quantity', 1))
    current = INVENTORY.get(sku, 0)
    if current < quantity:
        return jsonify(status='INSUFFICIENT_STOCK', sku=sku, available=current), 409
    INVENTORY[sku] = current - quantity
    return jsonify(status='RESERVED', sku=sku, reserved=quantity, remaining=INVENTORY[sku]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
