import json, requests
BASE_URL='https://fakestoreapi.com'

#get all products
#all_prod_response=requests.get(f"{BASE_URL}/products")
#print(all_prod_response.json())
#print(all_prod_response)

#for product in all_product_response.json:
#    print(f"{product['title']} costs ${product['price']}")

#get single product

#prod_5_response=requests.get(f"{BASE_URL}/products/5")
#print(prod_5_response.json())


#get prod with limit query param
# query_param={"limit" :3}
# prod_limit_res =requests.get(f"{BASE_URL}/products/",params=query_param)
# print(prod_limit_res.json())

#get sorted products with query params
# query_param={"sort":"desc"}
# prod_sort_response=requests.get(f"{BASE_URL}/products",params=query_param)
# print(prod_sort_response.json())

#get product categories
prod_category_response=requests.get(f"{BASE_URL}/products/categories")
print(prod_category_response.json())