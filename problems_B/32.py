x = input()
y = input()
res = ''
for k, v in enumerate(y):
    if v > x[k]:
        print(-1)
        break
    res += v

if len(res) == len(y):
    print(res)
