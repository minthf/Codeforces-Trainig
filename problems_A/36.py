n, d = map(int, input().split())
soldiers = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if abs(soldiers[i] - soldiers[j]) <= d:
            count += 1

print(count)
