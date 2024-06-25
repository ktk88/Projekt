import requests
print('Hello')
url = 'https://fakestoreapi.com/products/category/jewelery'
response = requests.get(url)
print (response.status_code)
print (response.json())