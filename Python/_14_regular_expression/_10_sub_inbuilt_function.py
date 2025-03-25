import re

mobile_no = "987-789-2672"  # 9877892672
res = re.sub("-","",mobile_no)
print(res)


import re

mobile_num = "987-789 2672"
res = re.sub("-| ","",mobile_num)
print(res)


import re

phone_no = '987-789 2672'
pattern = '\D'
result = re.sub(pattern, '',phone_no)

print(result)


import re

mobile_number = "987-789 2672"
res = re.sub("[-\s]", "", mobile_number)
print(res)



# 1800 0002 2020 # 18 2 22
import re

_no = "1800 0002 2020"

res = re.sub("0","",_no)
print(res)
