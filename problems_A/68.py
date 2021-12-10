n, m = map(int, input().split())
arr = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for i in range(1, tmp[0] + 1):
        arr.append(tmp[i])

if len(set(arr)) == m:
    print("YES")
else:
    print('NO')
