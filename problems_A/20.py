n = int(input())
people = []
for i in range(n):
    people.append(list(map(int, input().split())))

maximum = 0
count = 0
for i in people:
    count += i[1] - i[0]
    if maximum < count:
        maximum = count

print(maximum)
