t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] != i + 1:
            ind = arr.index(i+1)
            arr[i:ind+1] = arr[i:ind+1][::-1]
            break
    for i in arr:
        print(i, end=' ')
    print('')