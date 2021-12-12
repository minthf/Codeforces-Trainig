n = int(input())

game = list(map(int, input().split()))

sereja = 0
dima = 0

for i in range(n):
    if i % 2 == 0:
        if game[0] > game[-1]:
            sereja += game[0]
            del(game[0])
        else:
            sereja += game[-1]
            del(game[-1])
    else:
        if game[0] > game[-1]:
            dima += game[0]
            del(game[0])
        else:
            dima += game[-1]
            del(game[-1])

print(sereja, dima)
