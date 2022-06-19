import numpy as np
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_fibonacci_huge_test(n,m):
    FibArray = [0]*(n + 1)
    FibArray[0] = 0
    FibArray[1] = 1
    
    for ii in range(2,n + 1):
        FibArray[ii] = (FibArray[ii - 1] + FibArray[ii - 2]) % m
    return FibArray

def get_fibonacci_huge_Table(n,m):
    FibArray = [0]*(n + 1)
    FibArray[0] = 0
    FibArray[1] = 1
    
    for ii in range(2,n + 1):
        FibArray[ii] = (FibArray[ii - 1] + FibArray[ii - 2])
        
    ModTable = np.array(FibArray) % 1
    for ii in range(2, m):
        B = np.array(FibArray) % ii
        ModTable = np.vstack([ModTable,B])
    return ModTable


if __name__ == '__main__':
    n, m = map(int, input().split())
    #print(get_fibonacci_huge_test(n, m))
    print(get_fibonacci_huge_Table(n, m))
