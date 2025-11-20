import json
import uuid
import os
from datetime import datetime

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
    