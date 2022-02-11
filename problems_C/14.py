t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = []
    otr = []
    posit = False
    if arr[0] > 0:
        pos.append(arr[0])
        posit = True
    else:
        otr.append(arr[0])
    for i in range(1, n):
        if arr[i] > 0:
            if posit == True:
                if pos and pos[-1] < arr[i]:
                    del(pos[-1])
                    pos.append(arr[i])
            else:
                pos.append(arr[i])
            posit = True
        if arr[i] < 0:
            if posit == False:
                if otr and otr[-1] < arr[i]:
                    del(otr[-1])
                    otr.append(arr[i])
            else:
                otr.append(arr[i])
            posit = False
    print(sum(pos) + sum(otr))

