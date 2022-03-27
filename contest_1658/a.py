t = int(input())
for i in range(t):
    n = int(input())
    cosp = input()
    count = 0
    for i in range(n):
        if cosp[i] == '0':
            if i + 1 < n and cosp[i+1] == '0':
                count += 2
            if i + 2 < n and cosp[i+1] == '1' and cosp[i+2] == '0':
                count += 1
    print(count)