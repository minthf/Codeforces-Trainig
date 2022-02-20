import math
n, x, y = map(int, input().split())
arr = list(map(int, input().split()))
if x > y:
    print(n)
else:
    count = 0
    for i in arr:
        if x >= i:
            count += 1
    print(math.ceil(count/2))
