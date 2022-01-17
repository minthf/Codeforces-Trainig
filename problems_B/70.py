n = int(input())
s = set(input())
res = n - len(s)
if res + len(s) > 26:
    print(-1)
else:
    print(res)
