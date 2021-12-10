n, m = map(int, input().split())

count = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    for i in range(2 * m - 1):
        if i % 2 != 0:
            continue
        if tmp[i] == 1 or tmp[i + 1] == 1:
            count += 1

print(count)
