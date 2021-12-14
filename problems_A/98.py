numbers = list(map(int, input().split()))

summ = max(numbers)

del(numbers[numbers.index(summ)])

for i in numbers:
    print(sum(numbers) - summ - i, end=' ')
