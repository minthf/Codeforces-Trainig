def f(x):
    if x % 2 == 0:
        return x//2
    else:
        return  - x + f(x - 1)

n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    print(f(r) - f(l - 1))
