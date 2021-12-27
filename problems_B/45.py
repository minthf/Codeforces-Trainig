a, b = map(int, input().split())
s = input()
res = ''
count = 0

for k, v in enumerate(s):
    if count >= b:
        res += s[k:]
        break
    if k == 0:
        if v != '1' and a > 1:
            count += 1
            res += '1'
        elif a == 1:
            res += '0'
            count += 1
        elif v == '0':
            res += '0'
        else:
            res += '1'
    elif v != '0':
        count += 1
        res += '0'
    else:
        res += '0'

print(res)