t = int(input())
for i in range(t):
    o, t = map(int, input().split())
    summ = o + t * 2
    if o == 0:
        print(1)
    else:
        print(summ + 1)