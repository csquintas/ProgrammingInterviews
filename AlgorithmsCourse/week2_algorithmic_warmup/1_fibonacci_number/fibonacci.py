# Uses python3

def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

def calc_fib_fast(n):
    fibArray = [0]*(n+2)
    fibArray[0] = 0
    fibArray[1] = 1
    
    for i in range(2,n+1):
        fibArray[i] = fibArray[i-1] + fibArray[i-2]
    return fibArray[n]

    

n = int(input())
#print(calc_fib_naive(n))
print(calc_fib_fast(n))
