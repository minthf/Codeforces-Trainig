n = int(input())

for i in range(n):
    m = int(input())
    sport = sorted(list(map(int, input().split())))
    minimum = 10000

    for i in range(m-1):
        if abs(sport[i] - sport[i + 1]) < minimum:
            minimum = abs(sport[i] - sport[i + 1])

    print(minimum)
