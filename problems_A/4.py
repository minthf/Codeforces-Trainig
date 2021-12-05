n = int(input())
arr = []
if n % 2 == 0:
    for i in range(1, n+1):
        if i % 2 != 0:
            arr.append(i+1)
        else:
            arr.append(i-1)
    for i in arr:
        print(i, end=' ')
else:
    print(-1)
