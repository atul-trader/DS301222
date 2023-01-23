lst=[[4, 1, 6], [7, 8], [4, 10, 8]]
# desired output= [ [6,1,4] , [8,7] , [8,10,4] ]

reversed = []
for i in lst:
    new_lst = []
    for j in range(len(i)):
        new_lst.append(i.pop())
    reversed.append(new_lst)

print(reversed)