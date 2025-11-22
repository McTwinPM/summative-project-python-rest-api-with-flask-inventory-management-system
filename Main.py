#!/usr/bin/env python3

import argparse
import sys
import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

from CLI.Classes import Product




console = Console()

def display_products():
    try:
        response = requests.get("http://localhost:5000/inventory")
        response.raise_for_status()
        products = response.json()
        
        if not isinstance(products, list):
            console.print(f"[red]Error: Expected list, got {type(products)}[/red]")
            console.print(f"[yellow]Response: {products}[/yellow]")
            return
            
    except requests.exceptions.ConnectionError:
        console.print("[red]Error: Flask server is not running![/red]")
        console.print("[yellow]Start the server with: python API/server.py[/yellow]")
        return
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error fetching products: {e}[/red]")
        return
    except ValueError as e:
        console.print(f"[red]Error parsing JSON: {e}[/red]")
        return
    
    if not products:
        console.print("[yellow]No products in inventory.[/yellow]")
        return
    table = Table(title="Product Inventory")

    table.add_column("ID", justify="center", style="cyan", no_wrap=True)
    table.add_column("Barcode", justify="center", style="cyan", no_wrap=True)
    table.add_column("Product Name", style="magenta")
    table.add_column("Brand", style="green")
    table.add_column("Ingredients", style="yellow")
    table.add_column("Stock", justify="center", style="blue")
    table.add_column("Price", justify="right", style="green")

    for product in products:
        ingredients = product.get('ingredients', [])
        if isinstance(ingredients, list):
            ingredients = ", ".join(ingredients)
        elif isinstance(ingredients, str):
            ingredients = ingredients
        else:
            ingredients = "N/A"
        table.add_row(
            str(product.get('id', 'N/A')),
            str(product.get('barcode', 'N/A')),
            product['product_name'],
            product['brand'],
            ingredients,
            str(product.get('stock', 'N/A')),
            f"${product.get('price', 5.0):.2f}"
        )

    console.print(table)

def main():
    

    parser = argparse.ArgumentParser(
        description= "Food Inventory Management CLI"

    )
    subparser = parser.add_subparsers(dest='command', help='Available commands')

    #product commands
    product_parser = subparser.add_parser('product', help='Product related commands')
    product_subparsers = product_parser.add_subparsers(dest='product_command')

    #search product
    search_product = product_subparsers.add_parser('search', help='Search for a product')
    search_product.add_argument('query', help='Product name or barcode to search for')
    #create product 
    add_product = product_subparsers.add_parser('add', help='Add a new product')
    add_product.add_argument('name', help='Name of the product')
    add_product.add_argument('brand', help='Brand of the product')
    add_product.add_argument('ingredients', nargs='+', help='List of ingredients')
    #remove product
    remove_product = product_subparsers.add_parser('remove', help='Remove a product')
    remove_product.add_argument('id', help='ID of the product to remove')

    #update product
    update_product = product_subparsers.add_parser('update', help='Update a product')
    update_product.add_argument('id', help='ID of the product to update')
    update_product.add_argument('--status', type=int, help='New status of the product')
    update_product.add_argument('--price', type=float, help='New price of the product')
    update_product.add_argument('--stock', type=int, help='New stock quantity of the product')
    #list products
    product_subparsers.add_parser('list', help='List all products')

    args = parser.parse_args()

    #Handle commands
    if args.command == 'product':
        if args.product_command == 'add':
            new_product = Product(args.name, args.brand, args.ingredients)
            try:
                response = requests.post(
                    "http://localhost:5000/inventory",
                    json=new_product.to_dict()
                )
                if response.status_code == 201:
                    console.print(f"[green]Product '{args.name}' added successfully![/green]")
                else:
                    console.print(f"[red]Failed to add product: {response.json()}[/red]")
            except requests.exceptions.ConnectionError:
                console.print("[red]Error: Flask server is not running![/red]")
                
        elif args.product_command == 'remove':
            try:
                response = requests.delete(f"http://localhost:5000/inventory/{args.id}")
                if response.status_code == 200:
                    console.print(f"[red]Product with ID '{args.id}' removed successfully![/red]")
                else:
                    console.print(f"[red]Product with ID '{args.id}' not found![/red]")
            except requests.exceptions.ConnectionError:
                console.print("[red]Error: Flask server is not running![/red]")
                
        elif args.product_command == 'list':
            display_products()
            
        elif args.product_command == 'search':
            query = args.query
            try:
                if query.isdigit():
                    response = requests.get(f"http://localhost:5000/inventory/fetch-product?barcode={query}")
                else:
                    response = requests.get(f"http://localhost:5000/inventory/fetch-product?name={query}")
                
                if response.status_code == 200:
                    product = response.json()
                    panel = Panel.fit(
                        Text.from_markup(
                            f"[bold magenta]{product.get('product_name', 'N/A')}[/bold magenta]\n"
                            f"[green]Brand:[/green] {product.get('brand', 'N/A')}\n"
                            f"[yellow]Ingredients:[/yellow] {', '.join(str(i) for i in product.get('ingredients', []))}\n"
                        ),
                        title="Product Found",
                        border_style="blue"
                    )
                    console.print(panel)
                else:
                    console.print(f"[red]Product '{query}' not found![/red]")
            except requests.exceptions.ConnectionError:
                console.print("[red]Error: Flask server is not running![/red]")
                
        elif args.product_command == 'update':
            updates = {}
            if args.stock is not None:
                updates['stock'] = args.stock
            if args.price is not None:
                updates['price'] = args.price
            
            try:
                response = requests.patch(
                    f"http://localhost:5000/inventory/{args.id}",
                    json=updates
                )
                if response.status_code == 200:
                    console.print(f"[green]Product with ID '{args.id}' updated successfully![/green]")
                else:
                    console.print(f"[red]Product with ID '{args.id}' not found![/red]")
            except requests.exceptions.ConnectionError:
                console.print("[red]Error: Flask server is not running![/red]")
        else:
            console.print("[red]Invalid product command![/red]")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()