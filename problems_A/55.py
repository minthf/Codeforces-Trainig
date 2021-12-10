n = int(input())
points = []
for i in range(n):
    tmp = list(map(int, input().split()))
    points.append(tmp)

mishka = 0
chris = 0

for i in points:
    if i[0] > i[1]:
        mishka += 1
    elif i[0] < i[1]:
        chris += 1

if mishka > chris:
    print('Mishka')
elif mishka < chris:
    print('Chris')
else:
    print('Friendship is magic!^^')
