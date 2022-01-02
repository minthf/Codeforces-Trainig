n = int(input())
rooms = list(map(int, input().split()))
b = []

for i in range(1, n - 1):
    if rooms[i] == 0 and rooms[i - 1] == 1 and rooms[i + 1] == 1 and (i - 2 not in b):
        b.append(i)

print(len(b))
