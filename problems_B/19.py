n = int(input())

s = list(map(int, input().split()))
neg = 0
coins = 0
zeros = 0
for i in s:
    if i > 0:
        coins += i - 1
    elif i < 0:
        coins +=  - i - 1
        neg += 1
    else:
        zeros += 1

if neg % 2 != 0:
    if zeros:
        coins += 1
        zeros -= 1
    else:
        coins += 2
coins += zeros

print(coins)