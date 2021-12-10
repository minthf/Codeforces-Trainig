n = int(input())
numbers = ''
i = 1
while len(numbers) < n:
    numbers += str(i)
    i += 1

print(numbers[n - 1])