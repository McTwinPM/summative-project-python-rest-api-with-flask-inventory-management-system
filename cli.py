import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from scripts.product_fetcher import fetch_products

console = Console()

def display_products():
    products = fetch_products()
    table = Table(title="Product Inventory")

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Product Name", style="magenta")
    table.add_column("Brand", style="green")
    table.add_column("Ingredients", style="yellow")
    table.add_column("Status", justify="center", style="red")

    for product in products:
        ingredients = ", ".join(product['ingredients'])
        table.add_row(
            str(product.get('id', 'N/A')),
            product['product_name'],
            product['brand'],
            ingredients,
            str(product['status'])
        )

    console.print(table)
