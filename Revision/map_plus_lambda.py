cube = lambda x: x ** 3  

def fibonacci(n):
    # return a list of fibonacci numbers
    fib =  [0,1] # [0,1,1,2,3]
    for i in range(2,n): #5
        fib.append(fib[i-2] + fib[i-1]) # 0 + 1 = 1 | 1 + 2 = 2 | 2 + 3 = 3
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

   