n = int(input())

for i in range(n):
    s = int(input())
    numbers = list(map(int, input().split()))
    count_2 = 0
    count_1 = 0
    for i in range(s):
        if i % 2 == 0 and numbers[i] % 2 != 0:
            count_1 += 1
        if i % 2 != 0 and numbers[i] % 2 == 0:
            count_2 += 1
    
    print(count_2 if count_2 == count_1 else -1)
