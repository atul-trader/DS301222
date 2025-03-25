import json

json_obj = """{
    "name":"Ram",
    "male":true,
    "hobby":null,
    "qualification":"10th"
}"""

dict_obj = json.loads(json_obj)
print(dict_obj)