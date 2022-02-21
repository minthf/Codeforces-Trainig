import math
n, r = map(int, input().split())
a = (math.pi*(n-2))/n

ans = r * ((math.cos(a/2))/(1-math.cos(a/2)))
print(ans)