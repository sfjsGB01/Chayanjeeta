
import json 
import requests
BASE_URL='https://fakestoreapi.com'

# new_prod={
#     "title": 'test product',
#     "price": 13.5,
#     "description": 'lorem ipsum set',
#     "image": 'https://i.pravatar.cc',
#     "category": 'electronic'
#     }

# response=requests.post(f"{BASE_URL}/products",json=new_prod)
# print(response.json())

#update a product
# update_product={
#     "title": 'test product_1',
#     "price": 13.5,
#     "description": 'lorem ipsum set',
#     "image": 'https://i.pravatar.cc',
#     "category": 'electronic'
#     }
# response_up=requests.put(f"{BASE_URL}/products/1",json=update_product)
# print(response_up)

#get single product

prod_5_response=requests.get(f"{BASE_URL}/products/category")
print(prod_5_response.json())

#delete a product
# res= requests.delete(f"{BASE_URL}/products/10")
# print(res.json())
