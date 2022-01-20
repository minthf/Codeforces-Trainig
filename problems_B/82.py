n = int(input())
arr = list(map(int, input().split()))
per = [x for x in range(1, n + 1)]
count = 0
for i in range(n):
    for k in arr:
        if k == per[i]:
            count += 1
            break

print(n - count)
