from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)
ORDERS_URL = os.getenv('ORDERS_URL', 'http://orders:8001')
PAYMENTS_URL = os.getenv('PAYMENTS_URL', 'http://payments:8002')
STOCK_URL = os.getenv('STOCK_URL', 'http://stock:8003')
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')

@app.get('/health')
def health():
    return jsonify(status='ok', service='api-gateway', version=APP_VERSION), 200

@app.get('/ready')
def ready():
    return jsonify(status='ready', service='api-gateway'), 200

@app.get('/version')
def version():
    return jsonify(service='api-gateway', version=APP_VERSION), 200

@app.post('/orders')
def create_order():
    payload = request.get_json(force=True)
    stock = requests.post(f'{STOCK_URL}/reserve', json=payload, timeout=5)
    if stock.status_code != 200:
        return jsonify(error='stock reservation failed', details=stock.json()), 409
    order_resp = requests.post(f'{ORDERS_URL}/orders', json=payload, timeout=5)
    if order_resp.status_code != 201:
        return jsonify(error='order creation failed', details=order_resp.json()), 500
    payment_resp = requests.post(f'{PAYMENTS_URL}/charge', json=payload, timeout=5)
    if payment_resp.status_code != 200:
        return jsonify(error='payment failed', details=payment_resp.json()), 402
    body = order_resp.json()
    body['payment'] = payment_resp.json()
    body['stock'] = stock.json()
    return jsonify(body), 201

@app.get('/orders/<order_id>')
def get_order(order_id):
    r = requests.get(f'{ORDERS_URL}/orders/{order_id}', timeout=5)
    return jsonify(r.json()), r.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
