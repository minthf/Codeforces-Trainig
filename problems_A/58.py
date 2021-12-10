n, d = map(int, input().split())

enemies = []
for i in range(d):
    enemies.append(input())

count = 0
maximum = 0

for i in enemies:
    if i.count('1') == n:
        if count > maximum:
            maximum = count
        count = 0
    else:
        count += 1

if count > maximum:
    print(count)
else:
    print(maximum)


