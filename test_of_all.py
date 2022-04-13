import random

a = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [4, 5, 6], [7, 8, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7]]
b = [1,2,3,4,5]
alls = [1,2,3,4,5,7,8,9]
c = None
for k in a:
    count = 0
    for i in k :
        if i in b: count+=1
        if count == 2:
            if all(j in alls for j in k):
                continue
            else:
                for j in k:
                    if j not in alls:
                        c= j

print(c)
for i in range(1,10):
    print(i)
