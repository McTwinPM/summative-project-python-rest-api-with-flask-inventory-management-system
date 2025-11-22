# mock_inventory = []
import requests
# def fetch_openfoodfacts_data():
#     try:
        
#         response = requests.get(
#             "https://world.openfoodfacts.org/cgi/search.pl?search_terms=pizza&page_size=5&json=1", 
#             params={
#                 'search_terms': 'pizza',
#                 'page_size': 10,
#                 'json': 1
#             }
#         )
        
#         print(f"API Status Code: {response.status_code}")
#         if response.status_code == 200:
#             external_data = response.json()
#             for item in external_data.get('products', []):
#                 product = {
#                     'id': item.get('id', len(mock_inventory) + 1),
#                     'product_name': item.get('product_name', 'N/A'),
#                     'brand': item.get('brands', 'N/A'),
#                     'ingredients': item.get('ingredients_text', 'N/A').split(', '),
#                     'status': 1  # Default status
#                 }
#                 mock_inventory.append(product)
#     except Exception as e:
#         print(f"Error fetching data from OpenFoodFacts: {e}")

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