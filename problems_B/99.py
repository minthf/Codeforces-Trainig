import math
n = int(input())
x = math.ceil(math.sqrt(n))
y = math.floor(math.sqrt(n))

if x * y >= n:
    print(x + y)
else:
    print(x + y + 1)
