n = int(input())

for i in range(n):
    s = int(input())
    cnt1 = 0
    cnt2 = 0
    while s % 2 == 0:
        s /= 2
        cnt1 +=1 

    while s % 3 == 0:
        s /= 3
        cnt2 += 1

    if (s == 1 and cnt1 <= cnt2):
        print(2 * cnt2 - cnt1)
    else:
        print(-1)
