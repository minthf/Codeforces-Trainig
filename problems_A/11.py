n = int(input())
scores = list(map(int, input().split()))

minimum = scores[0]
maximum = scores[0]
count = 0
for i in scores:
    if i > maximum:
        count += 1
        maximum = i
    if i < minimum:
        count += 1
        minimum = i

print(count)
