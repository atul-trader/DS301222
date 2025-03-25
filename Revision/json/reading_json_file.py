import json

file = open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Revision\\json\\demo.json")

# it will read the data from demo.json file and convert it into dict
data = json.load(file)
print(data)