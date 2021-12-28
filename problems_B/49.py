n = int(input())
cont = sorted(list(map(int, input().split())))
count = 1
for i in range(n):
    if cont[i] >= count:
        count += 1

print(count - 1)


