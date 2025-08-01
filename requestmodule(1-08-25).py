import requests
print(requests)
# Dummy Json products:
api = "https://dummyjson.com/products"
data = requests.get(api)

products = data.json()
for i in products["products"]:
    print(i["id"],i["title"])
print()    


api ="https://fakestoreapi.in/api/products"
data = requests.get(api)
print(data)
products = data.json()
for i in products["products"]:
    print(i["id"],i["title"])
print()

# Dummy Json Quotes:
api1 = "https://dummyjson.com/quotes"
data1 = requests.get(api1)
posts = data1.json()
for j in posts["quotes"]:
    print(j["id"],j["quote"])