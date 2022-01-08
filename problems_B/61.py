n = int(input())
delit = [(2 ** x - 1) * (2 ** (x - 1)) for x in range(1,9)]

for i in delit[::-1]:
    if n % i == 0:
        print(i)
        break