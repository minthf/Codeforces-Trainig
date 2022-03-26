t = int(input())
for q in range(t):
    n = int(input())
    s = input()
    i = 0
    count = 0
    last = 0
    while i < n:
        if s[i] == '(' and i != n-1: 
            count += 1
            i += 2
            last = i
        else:
            i += 1
            while i < n:
                if s[i] == ')':
                    last = i + 1
                    count += 1
                    i += 1
                    break
                i += 1

    print(count, n-last)
