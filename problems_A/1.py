n = int(input())
count = 0

for i in range(n):
    team = list(map(int, input().split()))
    if team[0] + team[1] + team[2] >= 2:
        count += 1

print(count)
