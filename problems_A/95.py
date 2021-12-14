n = int(input())

for i in range(n):
    t = int(input())
    numbers = list(map(int, input().split()))
    tmp = []
    for k in numbers:
        if k not in tmp:
            print(k, end=' ')
            tmp.append(k)
    print(' ')
        
