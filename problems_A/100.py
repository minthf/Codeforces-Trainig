q = int(input())
for i in range(q):
    n = input()
    i = 0
    while n not in ['1', -1]:
        if n[-1] in ['0', '5']:
            n = str(int(n)*4//5)
        elif sum([int(x) for x in n]) % 3 == 0:
            n = str(int(n)*2//3)
        elif int(n[-1]) % 2 == 0:
            n = str(int(n)//2)
        else:
            n = -1
        i += 1

    print(-1 if n == -1 else i)
