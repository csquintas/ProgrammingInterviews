def max_pairwise_product(numbers):
    n = len(numbers)
    index_1 = 0
    
    for i in range(1,n):   #Scan for max
        if numbers[i]>numbers[index_1]:
            index_1 = i   
             
    if index_1 == 0:
        index_2 = 1
    else:
        index_2 = 0  
    
    for i in range(1,n):
        if ((numbers[i] != numbers[index_1]) & (numbers[i] > numbers[index_2])):
            index_2 = i
    product = numbers[index_1]*numbers[index_2]
    return product

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
