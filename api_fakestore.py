import pprint
import requests
from pprint import pformat
url_categories = 'https://fakestoreapi.com/products/categories'
url_products = 'https://fakestoreapi.com/products'
response_categories= requests.get(url_categories).json()
response_products= requests.get(url_products).json()
print('\n','*'*150, '\n')
print('Категории товаров, представленных на https://fakestoreapi.com:')

for i in range(len(response_categories)):
    print(f'{i+1}   {response_categories[i]}')
    i+=1

products_number = int(input('\n О товарах какой категории Вы хотите получить информацию (выберите номер категории из списка)?: '))
if products_number > i:
    print('Такой категории товаров не существует')
category = response_categories[products_number-1]

print(f'\n Товары категории "{category}"')
i=1
for item in response_products:
    if item["category"] == category:         
        print(f'\n {i}. Наименование товара: {item["title"]}')
        print(f'Цена: {item["price"]} $')
        description= pformat(item["description"], width=100)
        chars_to_remove = ["(", ")", "'"]
        for char in chars_to_remove:
            description = description.replace(char, "")
        print ('Описание товара: ') 
        print(description)
        print(f'Ссылка на изображение товара:  {item ["image"].upper()}') 
        print(f'Рейтинг товара: {item ["rating"]["rate"]}') 
        print(f'Количество на складе: {item ["rating"]["count"]}\n')
        i+=1
       
       