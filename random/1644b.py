t = int(input())
for i in range(t):
    n = int(input())
    for i in range(1, n+1):
        print(i, end=' ')
        for j in range(n, 0, -1):
            if i != j:
                print(j, end=' ')
        print('')