zabr, n = map(int, input().split())
tmp = []
for i in range(n):
    tmp.append(list(map(int, input().split())))

tmp.sort(key=lambda x: x[1], reverse=True)

summary = 0

for i in tmp:
    if zabr < i[0]:
        summary += i[1] * zabr
        break
    else:
        summary += i[1] * i[0]
        zabr -= i[0]

print(summary)
