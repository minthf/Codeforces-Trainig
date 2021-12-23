n = int(input())

for i in range(n):
    a = int(input())
    x = int((a + 3) / 4)
    res = '9' * int(a - x)
    res += '8' * int(x)
    print(res)
