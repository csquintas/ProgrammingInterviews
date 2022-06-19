# Uses python3
n = int(input())
lst = []
for _ in range(n):
    a, b = [int(i) for i in input().split()]
    lst.append((a,b))

lst.sort(key = lambda x: x[1]) #THIS SORTS IT BY THE SECOND ENTRY

index = 0
coordinates = []

while index < n:
    curr = lst[index]  #grabs (a,b)
    while index < n-1 and curr[1]>=lst[index+1][0]: # while not last entry and b1 >= a2
        index += 1
    coordinates.append(curr[1]) #add b1 to coordinates
    index += 1
print(len(coordinates))
print(' '.join([str(i) for i in coordinates]))