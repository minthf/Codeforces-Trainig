seg = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
a, b = map(int, input().split())
res = 0
x = 0
for i in range(a, b + 1):
    x = i
    while x:
        res += seg[x % 10]
        x //= 10

print(res)