def fibonacci(n):
    if n <= 1:
        return 1
    res = (fibonacci(n-1)+fibonacci(n-2))   # fibonacci(3)+fibonacci(2)  = 3 + 2
    print("Result : ",res)
    return  res

for i in range(10): # i = 4
    print("Fibonancci of : ",i)
    print(fibonacci(i))


# 1
# 1

