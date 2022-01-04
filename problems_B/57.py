n = int(input())
a = list(map(int, input().split()))
m = -1
found = True
for k, v in enumerate(a):
    if v > m + 1:
        print(k + 1)
        found = False
        break
    m = max(m, v)
if found:
    print(-1)