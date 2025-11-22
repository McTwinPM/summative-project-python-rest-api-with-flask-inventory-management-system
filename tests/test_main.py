import sys
import os
import pytest
from unittest.mock import Mock, patch, MagicMock
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CLI.Classes import Product

def test_product_initialization():
    """Test Product class initialization"""
    product = Product(
        barcode='123456789',
        product_name='Test Product',
        brand='Test Brand',
        ingredients=['ingredient1', 'ingredient2'],
        price=9.99
    )
    
    assert product.barcode == '123456789'
    assert product.product_name == 'Test Product'
    assert product.brand == 'Test Brand'
    assert product.ingredients == ['ingredient1', 'ingredient2']
    assert product.price == 9.99
    assert product.status == 1
    assert product.id is not None

def test_product_to_dict():
    """Test Product to_dict method"""
    product = Product(
        barcode='123456789',
        product_name='Test Product',
        brand='Test Brand',
        ingredients=['ingredient1', 'ingredient2'],
        price=9.99
    )
    
    product_dict = product.to_dict()
    
    assert product_dict['barcode'] == '123456789'
    assert product_dict['product_name'] == 'Test Product'
    assert product_dict['brand'] == 'Test Brand'
    assert product_dict['ingredients'] == ['ingredient1', 'ingredient2']
    assert product_dict['price'] == 9.99
    assert product_dict['status'] == 1
    assert 'id' in product_dict

def test_product_from_dict():
    """Test Product from_dict class method"""
    data = {
        'id': 'test-id-123',
        'barcode': '987654321',
        'product_name': 'From Dict Product',
        'brand': 'Dict Brand',
        'ingredients': ['test1', 'test2'],
        'status': 0,
        'price': 19.99
    }
    
    product = Product.from_dict(data)
    
    assert product.id == 'test-id-123'
    assert product.barcode == '987654321'
    assert product.product_name == 'From Dict Product'
    assert product.brand == 'Dict Brand'
    assert product.ingredients == ['test1', 'test2']
    assert product.status == 0

def test_change_status():
    """Test changing product status"""
    product = Product('123', 'Test', 'Brand', ['ing1'])
    
    assert product.status == 1
    product.change_status(0)
    assert product.status == 0
    product.change_status('1')
    assert product.status == 1

def test_update_price():
    """Test updating product price"""
    product = Product('123', 'Test', 'Brand', ['ing1'], price=10.0)
    
    assert product.price == 10.0
    product.update_price(15.99)
    assert product.price == 15.99
    product.update_price('20.50')
    assert product.price == 20.50

@patch('requests.post')
def test_mock_api_add_product(mock_post):
    """Test mocking API POST request to add product"""
    # Create a mock response
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {
        'id': 1,
        'barcode': '123456',
        'product_name': 'Mocked Product',
        'brand': 'Mock Brand',
        'ingredients': ['mock1', 'mock2'],
        'status': 1,
        'price': 5.99
    }
    mock_post.return_value = mock_response
    
    # Simulate adding a product
    import requests
    product = Product('123456', 'Mocked Product', 'Mock Brand', ['mock1', 'mock2'], 5.99)
    response = requests.post('http://localhost:5000/inventory', json=product.to_dict())
    
    # Assertions
    assert response.status_code == 201
    assert response.json()['product_name'] == 'Mocked Product'
    mock_post.assert_called_once()

@patch('requests.get')
def test_mock_api_get_inventory(mock_get):
    """Test mocking API GET request to fetch inventory"""
    # Create mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {
            'id': 1,
            'barcode': '111',
            'product_name': 'Product 1',
            'brand': 'Brand A',
            'ingredients': ['ing1'],
            'status': 1,
            'stock': 10
        },
        {
            'id': 2,
            'barcode': '222',
            'product_name': 'Product 2',
            'brand': 'Brand B',
            'ingredients': ['ing2'],
            'status': 1,
            'stock': 5
        }
    ]
    mock_get.return_value = mock_response
    
    # Simulate fetching inventory
    import requests
    response = requests.get('http://localhost:5000/inventory')
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]['product_name'] == 'Product 1'
    mock_get.assert_called_once_with('http://localhost:5000/inventory')

@patch('requests.patch')
def test_mock_api_update_product(mock_patch):
    """Test mocking API PATCH request to update product"""
    # Create mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'id': 1,
        'barcode': '123',
        'product_name': 'Updated Product',
        'brand': 'Updated Brand',
        'ingredients': ['new_ing'],
        'status': 0,
        'price': 12.99
    }
    mock_patch.return_value = mock_response
    
    # Simulate updating a product
    import requests
    updates = {'product_name': 'Updated Product', 'price': 12.99}
    response = requests.patch('http://localhost:5000/inventory/1', json=updates)
    
    # Assertions
    assert response.status_code == 200
    assert response.json()['product_name'] == 'Updated Product'
    assert response.json()['price'] == 12.99
    mock_patch.assert_called_once()

@patch('requests.delete')
def test_mock_api_delete_product(mock_delete):
    """Test mocking API DELETE request"""
    # Create mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {'message': 'Item deleted'}
    mock_delete.return_value = mock_response
    
    # Simulate deleting a product
    import requests
    response = requests.delete('http://localhost:5000/inventory/1')
    
    # Assertions
    assert response.status_code == 200
    assert response.json()['message'] == 'Item deleted'
    mock_delete.assert_called_once_with('http://localhost:5000/inventory/1')

@patch('requests.get')
def test_mock_external_api_openfoodfacts(mock_get):
    """Test mocking OpenFoodFacts external API"""
    # Create mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'status': 1,
        'product': {
            'code': '737628064502',
            'product_name': 'Nutella',
            'brands': 'Ferrero',
            'ingredients_text': 'Sugar, Palm Oil, Hazelnuts, Cocoa'
        }
    }
    mock_get.return_value = mock_response
    
    # Simulate fetching from OpenFoodFacts
    import requests
    response = requests.get('https://world.openfoodfacts.org/api/v2/product/737628064502.json')
    
    # Assertions
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 1
    assert data['product']['product_name'] == 'Nutella'
    assert data['product']['brands'] == 'Ferrero'