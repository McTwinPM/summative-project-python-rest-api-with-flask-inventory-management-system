from flask import Flask, jsonify, request
import requests
from CLI.Classes import Product

app = Flask(__name__)

#mock data
mock_inventory = []

def fetch_openfoodfacts_data():
    try:
        response = requests.get("https://world.openfoodfacts.net/api/v2/product/.json", headers={"Authorization": "Basic " + btoa("off:off")})
        if response.status_code == 200:
            external_data = response.json()
            for item in external_data.get('products', []):
                product = {
                    'id': item.get('id', len(mock_inventory) + 1),
                    'product_name': item.get('product_name', 'N/A'),
                    'brand': item.get('brands', 'N/A'),
                    'ingredients': item.get('ingredients_text', 'N/A').split(', '),
                    'status': 1  # Default status
                }
                mock_inventory.append(product)
    except Exception as e:
        print(f"Error fetching data from OpenFoodFacts: {e}")
fetch_openfoodfacts_data()

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(mock_inventory), 200

@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    mock_inventory.append(new_item)
    if 'id' not in new_item:
        new_item['id'] = len(mock_inventory)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in mock_inventory if item['id'] == item_id), None)
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
    