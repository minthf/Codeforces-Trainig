n, k = map(int, input().split())
s = input()
arr = list(input().split())
counts = []
tmp = 0
for i in s:
    if i in arr:
        tmp += 1
    else:
        counts.append(tmp)
        tmp = 0
if tmp:
    counts.append(tmp)
summary = 0
for n in counts:
    summary += n*(n+1)//2
print(summary)