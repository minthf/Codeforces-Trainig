n = int(input())

chrono = list(map(int, input().split()))

count = 0

summ = 0

for i in chrono:
    summ += i
    if summ < 0:
        count += 1
        summ = 0

print(count)