n = int(input())
arr = sorted(list(map(int, input().split())))

print(min(arr[n-2] - arr[0], arr[n - 1] - arr[1]))
