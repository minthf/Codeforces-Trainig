t = int(input())

for i in range(t):
    n = int(input())
    tmp = input()
    res = ''
    for i in range(n):
        res += tmp[2 * i]
    print(res)
