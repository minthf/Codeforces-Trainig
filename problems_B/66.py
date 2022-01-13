n = int(input())
arr = sorted(list(map(int, input().split())))
found = True
for i in range(1, n - 1):
    if arr[i - 1] + arr[i] > arr[i + 1]:
        print('YES')
        found = False
        break

if found:
    print('NO')
    