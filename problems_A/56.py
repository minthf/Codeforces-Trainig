n = int(input())
numbers = list(map(int, input().split()))

count = 1
maximum = 0

for k, v in enumerate(numbers[:-1]):
    if numbers[k + 1] > v:
        count += 1
    else:
        if count > maximum:
            maximum = count

        count = 1

if count > maximum:
    print(count)
else:
    print(maximum)
