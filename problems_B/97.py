t = int(input())
for i in range(t):
    n = int(input())
    days = list(map(int, input().split()))
    count = 0
    minimum = days[-1]
    for i in range(n-1, -1, -1):
        if days[i] > minimum:
            count += 1
        if days[i] < minimum:
            minimum = days[i]

    print(count)
