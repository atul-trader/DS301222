# List Comprehension - creating a list out of another list

# for i in lst:
#     if <condtion>:
#         body

# [body for i in lst if <condition>]

nums = [4,7,4,8,9,4,2,4]

# lst = []
# for i in nums:
#     lst.append(i)

# print(lst)

# lst = [i for i in nums]
# print(lst)



# even_list = []
# for i in nums:
#     if i%2==0:
#         even_list.append(i)

# print(even_list)

# even_list = [i for i in nums if i%2==0]
# print(even_list)



# items = ["apple","mango","laptop","mobile","aeroplane","ac","diary"]
# new_lst = [i for i in items if i.startswith("a") and len(i)>=4]
# print(new_lst)


nums = [4,7,14,8,9,40,2,14]
# 0,2,5,7
# [4,14,40,14]

nums = [4, 7, 14, 8, 9, 40, 2, 14]
new_list = [nums[i] for i in [0, 2, 5, 7]]
print("Elements at positions 0, 2, 5, and 7:", new_list)


