n = int(input())
s = input()
res = []
while n != 0:
    if (n % 2 == 1):
        res.append(s[0])
    else:
        res = list(s[0]) + res
    s = s[1:]
    n -= 1

print(''.join(res))

