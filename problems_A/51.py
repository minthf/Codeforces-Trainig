n, c = map(int, input().split())
words = list(map(int, input().split()))

count = 0

for k, v in enumerate(words[:-1]):
    if words[k + 1] - v > c:
        count = 0
    else:
        count += 1

print(count + 1)