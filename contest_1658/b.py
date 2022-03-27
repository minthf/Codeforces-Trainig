import math
t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 != 0:
        print(0)
    else:
        tmp = math.factorial(n//2)
        print(tmp * tmp %  998244353)
