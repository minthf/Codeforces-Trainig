limak, bob = map(int, input().split())
i = 0
while limak <= bob:
    limak *= 3
    bob *= 2
    i += 1

print(i)
