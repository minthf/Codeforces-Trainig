t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    tmp = [True if arr.count(i+1) > 0 else False for i in range(2*n)] 
    # print(tmp)
    err = False
    count = 0
    for i in range(2*n):
        if count < 0:
            break
        if tmp[i] == True:
            count += 1
        else:
            count -= 1
    if count == -1:
        print(-1)
    else:
        tmp = [x for x in range(1, n*2 + 1) if x not in arr]
        for i in arr:
            print(i, end=' ')
            for k in range(len(tmp)):
                if tmp[k] > i:
                    print(tmp[k], end=' ')
                    del(tmp[k])
                    break
        print('')





        