def max_pairwise_product(numbers):
    p1 = max(numbers)
    numbers.remove(p1)
    p2 = max(numbers)
    return p1*p2

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))