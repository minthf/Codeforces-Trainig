n, k = map(int, input().split())

a = 240 - k
found = True
for i in range(1, n + 1):
    if a - i * 5 < 0:
        print(i - 1)
        found = False
        break
    a -= i * 5

if found:
    print(i)