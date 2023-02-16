import json

# with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\_22_json_file_handling\\test.json") as file:
#     # it reads the data from the json file and converts it into dict
#     data = json.load(file)
#     print(data)
#     print(type(data))

data = {
    "rno":1,
    "name":"Raj",
    "female":False,
    "male":True,
    "job":None
}

with open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Python\\_22_json_file_handling\\write.json","w") as file:
    # converting dict into json and then storing it in json file
    json.dump(data,file)