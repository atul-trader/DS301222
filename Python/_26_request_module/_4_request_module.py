import requests

url = "https://jsonplaceholder.typicode.com/todos"

data = {
    "rno" : "101",
    "name" : "Raj"
}

# first way
response = requests.request("POST",url,json=data).json()
print(response)

# second way
response = requests.post(url,json=data).json()
print(response)