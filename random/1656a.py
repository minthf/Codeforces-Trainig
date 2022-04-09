t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    mini = 0
    minimum = 1e9+1
    maxi = 0
    maximum = -1
    for i in range(n):
        if arr[i] > maximum:
            maxi = i + 1
            maximum = arr[i]
        if arr[i] < minimum:
            mini = i + 1
            minimum = arr[i]
    print(mini, maxi)

