# Uses python3
"""
n = int(input())

lst = [1]

index = 0

while sum(lst) < n:
    nextnum = lst[index] + 1
    nextnextnum = nextnum + 1
    if (sum(lst) + nextnum + nextnextnum) <= n:
        lst.append(nextnum)
        index += 1
    else:
        lastnum = n - sum(lst) 
        lst.append(lastnum)

if n == 2:
    lst = [2]    

print(len(lst))
print(' '.join([str(i) for i in lst]))
"""

n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()
W = n
prizes = []
for i in range(1, n):
    if W>2*i:
        prizes.append(i)
        W -= i
    else:
        prizes.append(W)
        break

print(len(prizes))
print(' '.join([str(i) for i in prizes]))
