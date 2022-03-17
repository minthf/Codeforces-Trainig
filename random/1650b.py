t = int(input())
for i in range(t):
    l, r, a = map(int, input().split())
    # for x in range(l, r+1):
    #     print(int(x/a) + x%a)
    if r >= a:
        tmp = r // a
        x = tmp * a - 1
        if x < l:
            x = r
        if r - tmp * a == a - 1:
            x = tmp * a + a-1
        print(int(x/a) + x%a)
    else:
        print(int(r/a) + r%a)
    
            