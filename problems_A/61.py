n, h = map(int, input().split())
guys = list(map(int, input().split()))

count = 0

for i in guys:
    if i > h:
        count += 2
    else:
        count += 1

print(count)
