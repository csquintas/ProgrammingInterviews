# Uses python3

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_last_digit_fast(n):
    FibArray = [0]*(n + 1)
    FibArray[0] = 0
    FibArray[1] = 1
    
    for ii in range(2,n + 1):
        FibArray[ii] = (FibArray[ii - 1] + FibArray[ii - 2]) % 10
    return FibArray[n]

if __name__ == '__main__':
    n = int(input())
    #print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))
    