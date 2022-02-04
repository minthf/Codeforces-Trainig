t = int(input())
for i in range(t):
    n = int(input())
    arr = [0 for x in range(1, n + 1)]
    a = list(map(int, input().split()))
    for i in a:
        arr[i - 1] += 1
    maxi = max(arr)
    count = n - arr.count(0)
    print(max(min(maxi - 1, count), min(maxi, count - 1)))
