t = int(input())
for i in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    even = []
    odd = []
    for i in range(n * 2):
        if numbers[i] % 2 == 0:
            even.append(i + 1)
        else:
            odd.append(i + 1)

    if len(even) % 2 != 0:
        for i in range(0, len(even) - 1, 2):
            print(even[i], even[i + 1])
        for i in range(0, len(odd) - 1, 2):
            print(odd[i], odd[i + 1])
    elif len(odd) == 0:
        for i in range(0, len(even) - 3, 2):
            print(even[i], even[i + 1])
    elif len(even) == 0:
        for i in range(0, len(odd) - 3, 2):
            print(odd[i], odd[i + 1])
    else:
        for i in range(0, len(even) - 1, 2):
            print(even[i], even[i + 1])
        for i in range(0, len(odd) - 3, 2):
            print(odd[i], odd[i + 1])

