import base64
from flask import Flask, jsonify, request
import requests
try:
    from inventory_data import fetch_product_by_barcode, fetch_product_by_name, mock_inventory
except ModuleNotFoundError:
    from API.inventory_data import fetch_product_by_barcode, fetch_product_by_name, mock_inventory
app = Flask(__name__)




@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(mock_inventory), 200

@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    new_item.setdefault('product_name', 'N/A')  # Default name if not provided
    new_item.setdefault('brand', 'N/A')  # Default brand if not provided
    new_item.setdefault('status', 1)  # Default status if not provided
    new_item.setdefault('ingredients', [])  # Default ingredients if not provided
    if 'id' not in new_item:
        new_item['id'] = len(mock_inventory) + 1
    mock_inventory.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in mock_inventory if item.get('id') == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((item for item in mock_inventory if item.get('id') == item_id), None)
    if item:
        updates = request.get_json()
        item.update(updates)
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global mock_inventory
    mock_inventory = [item for item in mock_inventory if item.get('id') != item_id]
    return jsonify({'message': 'Item deleted'}), 200


@app.route('/inventory/fetch-product', methods=['GET'])
def fetch_external_api():
    name = request.args.get('name')
    barcode = request.args.get('barcode')
    product = None
    if barcode:
        product = fetch_product_by_barcode(barcode)
    elif name:
        product = fetch_product_by_name(name)
    
    if product:
        inventory_item = {
            'id': len(mock_inventory) + 1,
            'product_name': product.get('product_name', 'Unknown'),
            'brand': product.get('brands', 'Unknown'),
            'ingredients': product.get('ingredients_text', '').split(', ') if product.get('ingredients_text') else ['N/A'],
            'stock': 10
        }
        return jsonify(inventory_item), 200
    else:
        return jsonify({'error': 'Product not found'}), 404
if __name__ == '__main__':
    app.run(debug=True)
    