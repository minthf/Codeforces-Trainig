n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    arr = []
    for i in range(a):
        arr.append(input())
    count = 0

    for i in range(a-1):
        if arr[i][-1] != 'D':
            count += 1

    for i in range(b-1):
        if arr[-1][i] != 'R':
            count += 1
    print(count)
