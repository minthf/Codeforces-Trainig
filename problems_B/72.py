n = int(input())
arr = sorted(list(map(int, input().split())))
res = []
for i in range(n//2):
    res.append(arr[i])
    res.append(arr[- 1 - i])

if n % 2 != 0:
    res.append(arr[n//2])

for i in res:
    print(i, end=' ')
print('')


