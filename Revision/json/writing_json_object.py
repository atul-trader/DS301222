import json

dict_obj = {
    "rno":1,
    "name":"Ram",
    "male":True,
    "hobby":None,
}

data = json.dumps(dict_obj)
print(data)