#Uses python3



def max_dot_product(a, b, n):
    a.sort() #sort is done in place!
    b.sort()     
    total = 0
    for ii in range(0,n):
        total = total + (a[ii] * b[ii])
    return total

if __name__ == '__main__':
    n = int(input()) #length of list
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(max_dot_product(a, b, n))
    
