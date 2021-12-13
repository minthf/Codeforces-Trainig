n = int(input())

count_left = 0
count_right = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    if tmp[0] > 0:
        count_right += 1
    else:
        count_left += 1

if min(count_left, count_right) in [1, 0]:
    print('Yes')
else:
    print('NO')
