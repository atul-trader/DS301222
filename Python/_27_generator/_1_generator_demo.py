# Generators

# generators are function
# it is memory efficient
# it doesn't allocate memory to all the objects at the same time
# it yields the data and returns the element of tha data when it is demanded

def fun(no):
    yield no*2

result = fun(10)
print(next(result))

# [ 4, 6, 8, 10, 12, 14, 16, 18, 20]
gen = (2*i for i in range(1,11))
print(next(gen))
print(next(gen))

