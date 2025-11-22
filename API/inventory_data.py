import requests

mock_inventory = []


real_url = "https://world.openfoodfacts.org"

def fetch_product_by_barcode(barcode: str):
    url = f'{real_url}/api/v2/product/{barcode}.json'
    resp = requests.get(url)
    if resp.ok and resp.json().get('status') == 1:
        return resp.json()['product']
    return None


def fetch_product_by_name(name: str):
    url = f'{real_url}/cgi/search.pl'
    params = {'search_terms': name,
              'search_simple': 1, 'json': 1, 'page_size': 1}
    resp = requests.get(url, params=params)
    data = resp.json()
    if data.get('products'):
        return data['products'][0]
    return None

def populate_inventory_with_many_products(max_products=50):
    """Fetch multiple pages of products from API"""
    try:
        products_fetched = 0
        page = 1
        page_size = 20
        
        while products_fetched < max_products:
            response = requests.get(
                f'{real_url}/cgi/search.pl',
                params={
                    'search_terms': '',  
                    'page': page,
                    'page_size': page_size,
                    'json': 1
                }
            )
            
            if response.status_code == 200:
                data = response.json()
                products = data.get('products', [])
                
                if not products:  
                    break
                
                for product in products:
                    if products_fetched >= max_products:
                        break
                        
                    inventory_item = {
                        'id': len(mock_inventory) + 1,
                        'barcode': product.get('code', f'unknown-{products_fetched}'),
                        'product_name': product.get('product_name', 'Unknown Product'),
                        'brand': product.get('brands', 'Unknown Brand'),
                        'ingredients': product.get('ingredients_text', '').split(', ') if product.get('ingredients_text') else ['N/A'],
                        'status': 1,
                        'stock': 10
                    }
                    mock_inventory.append(inventory_item)
                    products_fetched += 1
                
                page += 1
            else:
                print(f"Failed to fetch page {page}")
                break
        
        print(f"✓ Loaded {len(mock_inventory)} products into inventory")
        
    except Exception as e:
        print(f"Error populating inventory: {e}")

# Actually call the function to populate on module load
populate_inventory_with_many_products(max_products=50)