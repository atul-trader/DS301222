# ChainMap
# used to combine multiple dictionary together

from collections import ChainMap

dict1 = {"a":"A","b":"B"}
dict2 = {1:"One",2:"Two"}
dict3 = {"rno":1,"name":"Bharati"}

chain_map = ChainMap(dict1,dict2,dict3)
print(chain_map)

dict4 = {"xyz":"xyz"}
dict5 = {"abc":"abc"}

chain_map1 = chain_map.new_child([dict4,dict5])
print(chain_map1)

