n = int(input())

for i in range(n):
    s = int(input())
    found = True
    babushki = sorted(list(map(int, input().split())))
    for i in range(s-1, -1, -1):
        if babushki[i] <= i + 1:
            print(i + 2)
            found = False
            break
    if found:
        print(1)
