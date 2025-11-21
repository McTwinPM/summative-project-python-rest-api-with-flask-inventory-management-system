#!/usr/bin/env python3

import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from server import mock_inventory, fetch_openfoodfacts_data
from CLI.Classes import Product

console = Console()

def display_products():
    products = mock_inventory
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

def main():
    fetch_openfoodfacts_data()
    display_products()

    parser = argparse.ArgumentParser(
        description= "Food Inventory Management CLI"
    )
    subparser = parser.add_subparsers(dest='command', help='Available commands')

    product_parser = subparser.add_parser('product', help='Product related commands')
    product_subparsers = product_parser.add_subparsers(dest='product_command')

    add_product = product_subparsers.add_parser('add', help='Add a new product')
    add_product.add_argument('name', required=True, help='Name of the product')
    add_product.add_argument('brand', required=True, help='Brand of the product')
    add_product.add_argument('ingredients', nargs='+', help='List of ingredients')

    remove_product = product_subparsers.add_parser('remove', help='Remove a product')
    remove_product.add_argument('id', required=True, help='ID of the product to remove')

    product_subparsers.add_parser('list', help='List all products')

    args = parser.parse_args()

    #Handle commands
    if args.command == 'product':
        if args.product_command == 'add':
            new_product = Product(args.name, args.brand, args.ingredients)
            mock_inventory.append(new_product.to_dict())
            console.print(f"[green]Product '{args.name}' added successfully![/green]")
        elif args.product_command == 'remove':
            product_to_remove = next((p for p in mock_inventory if p['id'] == args.id), None)
            if product_to_remove:
                mock_inventory.remove(product_to_remove)
                console.print(f"[red]Product with ID '{args.id}' removed successfully![/red]")
            else:
                console.print(f"[red]Product with ID '{args.id}' not found![/red]")
        elif args.product_command == 'list':
            display_products()
        else:
            console.print("[red]Invalid product command![/red]")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()