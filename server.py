import base64
from flask import Flask, jsonify, request
import requests
from inventory_data import fetch_product_by_barcode, fetch_product_by_name

app = Flask(__name__)




@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(app.inventory), 200

@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    mock_inventory.append(new_item)
    if 'id' not in new_item:
        new_item['id'] = len(mock_inventory)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in app.inventory if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((item for item in mock_inventory if item['id'] == item_id), None)
    if item:
        updates = request.get_json()
        item.update(updates)
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global mock_inventory
    mock_inventory = [item for item in mock_inventory if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
    