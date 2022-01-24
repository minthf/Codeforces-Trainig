t = int(input())
for i in range(t):
    n = int(input())
    h = 1
    count = 0
    while n >= 2:
        tmp = (3 * h ** 2) / 2 + h / 2
        if n < tmp:
            count += 1
            h -= 1
            n -= (3 * h ** 2) / 2 + h / 2
            h = 0
        else:
            h += 1

    print(count)