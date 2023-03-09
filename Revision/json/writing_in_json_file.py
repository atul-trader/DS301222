import json

file = open("C:\\Users\\vashi\\OneDrive\\Documents\\DS301222\\Revision\\json\\test.json","w")

data = {
    "rno":1,
    "name":"Ram",
    "male":True,
    "hobby":None,
}

json.dump(data,file)
