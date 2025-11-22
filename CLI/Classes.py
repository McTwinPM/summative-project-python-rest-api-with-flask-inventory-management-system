import json
import uuid
import os
from datetime import datetime
from inventory_data import mock_inventory

class Product:
    def __init__(self, product_name, brand, ingredients):
        self.id = str(uuid.uuid4())
        self.product_name = product_name
        self.brand = brand
        self.ingredients = ingredients
        self.status = 1  # Default status

    def to_dict(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'brand': self.brand,
            'ingredients': self.ingredients,
            'status': self.status
        }
    def remove(self):
        product_dict = self.to_dict()
        if product_dict in mock_inventory:
            mock_inventory.remove(product_dict)
    @classmethod
    def from_dict(cls, data):
        product = cls(
            product_name=data.get('product_name', 'N/A'),
            brand=data.get('brand', 'N/A'),
            ingredients=data.get('ingredients', [])
        )
        product.id = data.get('id', str(uuid.uuid4()))
        product.status = data.get('status', 1)
        return product
    
    def change_status(self, new_status):
        self.status = int(new_status)