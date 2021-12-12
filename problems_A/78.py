cal = list(map(int, input().split()))

game = input()

summary = 0

for i in game:
    summary += cal[int(i) - 1]

print(summary)
