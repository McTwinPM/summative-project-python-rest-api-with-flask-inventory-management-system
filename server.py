from flask import Flask, jsonify, request

app = Flask(__name__)

#mock data
mock_api = [{'status': 1, 'product': {'product_name': 'pizza', 'brand': 'Digorno', 'ingredients': ['cheese', 'sauce', 'dough']}},
        {'status': 2, 'product': {'product_name': 'burger', 'brand': 'McDonalds', 'ingredients': ['bun', 'patty', 'lettuce']}}]

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(mock_api), 200

@app.route('/inventory', methods=['POST'])
def add_item():
    new_item = request.get_json()
    mock_api.append(new_item)
    return jsonify(new_item), 201

@app.route('/inventory/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in mock_api if item['id'] == item_id), None)
    if item:
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/inventory/<int:item_id>', methods=['PATCH'])
def update_item(item_id):
    item = next((item for item in mock_api if item['id'] == item_id), None)
    if item:
        updates = request.get_json()
        item.update(updates)
        return jsonify(item), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/inventory/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global mock_api
    mock_api = [item for item in mock_api if item['id'] != item_id]
    return jsonify({'message': 'Item deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
    