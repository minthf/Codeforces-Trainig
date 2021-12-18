n = int(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(n):
    a, b, c = map(int, input().split())
    sub = alpha[:c]
    res = sub * a
    res = res[:a]
    print(res)


