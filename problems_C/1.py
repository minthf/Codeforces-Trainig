n = int(input())
for i in range(n):
    t = int(input())
    s = input()
    res = 0
    count = 0
    for i in s:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
            if count < 0:
                count = 0
                res += 1

    print(res)
