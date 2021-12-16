n = int(input())

for i in range(n):
    s = input()
    ones = sorted([x for x in s.split('0') if x != ''])[::-1]
    points = 0
    for i in range(len(ones)):
        if i % 2 == 0:
            points += len(ones[i])
    print(points)
