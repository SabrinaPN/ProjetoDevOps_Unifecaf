from flask import Flask, jsonify, request
import os
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB_PATH = os.getenv('DB_PATH', '/tmp/orders.db')
APP_VERSION = os.getenv('APP_VERSION', '1.0.0')

Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY AUTOINCREMENT, customer TEXT, sku TEXT, quantity INTEGER, status TEXT)')
    conn.commit()
    conn.close()

init_db()

@app.get('/health')
def health():
    return jsonify(status='ok', service='orders', version=APP_VERSION), 200

@app.get('/ready')
def ready():
    return jsonify(status='ready', service='orders'), 200

@app.post('/orders')
def create_order():
    payload = request.get_json(force=True)
    customer = payload.get('customer', 'unknown')
    sku = payload.get('sku', 'SKU-001')
    quantity = int(payload.get('quantity', 1))
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('INSERT INTO orders (customer, sku, quantity, status) VALUES (?, ?, ?, ?)', (customer, sku, quantity, 'CREATED'))
    order_id = cur.lastrowid
    conn.commit()
    conn.close()
    return jsonify(order_id=order_id, status='CREATED', customer=customer, sku=sku, quantity=quantity), 201

@app.get('/orders/<order_id>')
def get_order(order_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT id, customer, sku, quantity, status FROM orders WHERE id = ?', (order_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return jsonify(error='order not found'), 404
    return jsonify(order_id=row[0], customer=row[1], sku=row[2], quantity=row[3], status=row[4]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
