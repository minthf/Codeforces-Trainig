a, b, c = map(int, input().split())
count = 0
for i in range(1, c + 1):
    if i % a == 0 and i % b == 0:
        count += 1

print(count)
