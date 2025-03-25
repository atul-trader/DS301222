import requests

url = "https://mocki.io/v1/d4867d8b-b5d5-4a48-a4ab-79131b5809b8"

# first way
response = requests.request("GET",url).json()
print(response)

# send way
response = requests.get(url).json()
print(response)

print()

print(response[3]["name"])

print()

print(response[-1]["name"])
