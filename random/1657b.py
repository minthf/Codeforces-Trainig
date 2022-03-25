t = int(input())
for i in range(t):
    n, b, x, y = map(int, input().split())
    arr = [0]
    summary = 0
    for i in range(1, n+1):
        if arr[i-1] + x <= b:
            arr.append(arr[i-1] + x)
        else:
            arr.append(arr[i-1] - y)
        summary += arr[-1]

    print(summary)