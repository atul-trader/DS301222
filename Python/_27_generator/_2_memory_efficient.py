import memory_profiler as memory

# def fun(n):
#     lst = []
#     for i in range(n):
#         lst.append(i)
#     return lst

# print("Before calling the function : ",memory.memory_usage())
# fun(10000000)
# print("After calling the function : ",memory.memory_usage())

def gen(n):
    for i in range(n):
        yield i

print("Before calling the function : ",memory.memory_usage())
gen(10000000)
print("After calling the function : ",memory.memory_usage())

    
