# size = int(input("Enter size : ")) # 3

# actual_lst = []
# for i in range(size):
#     lst = []
#     for j in range(2):
#         element = int(input("Enter element : "))
#         lst.append(element)
#     actual_lst.append(lst)

# print(actual_lst)

# tup_list = []
# for i in actual_lst:
#     tup_list.append(tuple(i))

# print(tup_list)



# tup = [(2,5),(1,2),(4,4),(2,3),(2,1)]
# for i in range(len(tup)): # i=0 
#     for j in range(len(tup)-i-1): # j=0               # 5-0-1 = 4
#         if(tup[j][-1]>tup[j+1][-1]):
#             temp = tup[j]           # temp = (2,5)
#             tup[j] = tup[j +1]      # tup[j] = (1,2)
#             tup[j+1] = temp         # tup[j+1] = (2,5)
# print(tup)

# [5,2,6,7,1]
# [2,5,6,7,1]
# [2,1,6,7,5]
# [1,2,6,7,5]
# [1,2,5,7,6]
# [1,2,5,6,7]



x = 'happy'



def summation():

    print(x)

    x = 'sad'



summation()