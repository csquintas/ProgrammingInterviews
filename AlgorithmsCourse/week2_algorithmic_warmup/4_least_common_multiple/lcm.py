# Uses python3

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def lcm_fast(a,b):
    #LCM is (a*b)/GCD(a,b)
    GCD = EuclidGCD(a, b)
    LCM = int((a * b)/GCD)
    return LCM
    
def EuclidGCD(a,b):
    if b == 0:
        return a
    a_prime = a % b
    return EuclidGCD(b,a_prime)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

