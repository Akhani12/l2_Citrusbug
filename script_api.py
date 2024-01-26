import requests


# Calling the get api to list the data ....
headers = {"context-data": "app/multipart"}
r_get = requests.get("http://127.0.0.1:5654/get_data/", headers= headers)

if r_get.status_code == 200:
    print(r_get.json())

# Calling the post api to store the data ....
headers = {"context-data": "app/multipart"}
data = {"name": "harsh", "age": 25}
r_post = requests.post("http://127.0.0.1:5654/store_data", json=data)

if r_post.status_code == 200:
    print(r_post.json())