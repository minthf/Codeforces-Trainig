n, m = map(int, input().split())

tel = sorted(list(map(int, input().split())))

summary = 0
for i in range(m):
    if tel[i] > 0:
        break
    summary -= tel[i]

print(summary)

