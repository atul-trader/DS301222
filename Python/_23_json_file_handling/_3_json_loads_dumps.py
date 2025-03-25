import json

json_obj = """{
    "name":"Bharati",
    "female":true,
    "designer":false,
    "hobbies":null
}"""

# converts json into dict
dict_obj = json.loads(json_obj)
print(dict_obj)
print(type(dict_obj))

# converts dict into json
json_obj = json.dumps(dict_obj)
print(json_obj)
