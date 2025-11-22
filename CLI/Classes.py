import json
import uuid
import os
from datetime import datetime

class Product:
    def __init__(self, barcode, product_name, brand, ingredients, price=0.0):
        self.id = str(uuid.uuid4())
        self.barcode = barcode
        self.product_name = product_name
        self.brand = brand
        self.ingredients = ingredients
        self.status = 1  
        self.price = price

    def to_dict(self):
        return {
            'id': self.id,
            'barcode': self.barcode,
            'product_name': self.product_name,            
            'brand': self.brand,
            'ingredients': self.ingredients,
            'status': self.status,
            'price': self.price  
        }

    @classmethod
    def from_dict(cls, data):
        product = cls(
            barcode=data.get('barcode', 'N/A'),
            product_name=data.get('product_name', 'N/A'),
            brand=data.get('brand', 'N/A'),
            ingredients=data.get('ingredients', [])
        )
        product.id = data.get('id', str(uuid.uuid4()))
        product.status = data.get('status', 1)
        return product
    
    def change_status(self, new_status):
        self.status = int(new_status)
    

    def update_price(self, new_price):
        self.price = float(new_price)