n = int(input())

rates = sorted(list(map(int, input().split())))

summary = sum(rates)
count = 0
i = 0
while True:
    if summary / n >= 4.5:
        print(count)
        break
    summary -= rates[i] - 5
    rates[i] = 5
    i += 1
    count += 1
