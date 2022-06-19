import math

def binary_search(A, low, high, key):
    if low > high:
        return -1
    mid = low + ((high - low)/2)
    mid = int(math.floor(mid))
    if key == A[mid]:
       return mid
    elif key < A[mid]:
       return binary_search(A, low , mid-1, key)
    else:
       return binary_search(A, mid+1, high, key)


if __name__ == '__main__':
    #num_keys = int(input("Enter how long of a list: "))
    #input_keys = list(map(int, input("Enter the sorted list: ").split()))
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    #num_queries = int(input("Enter how many keys you would like to find: "))
    #input_queries = list(map(int, input("Enter the keys: ").split()))
    num_queries = int(input())
    input_queries = list(map(int, input().split()))    
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, 0, (num_keys-1), q), end=' ')
