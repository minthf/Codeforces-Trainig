a = int(input())
w, h = map(int, input().split())

k = max(w, h)
b = True
for i in range(a-1):
    w1, h1 = map(int, input().split())
    maxi = max(w1, h1)
    mini = min(w1, h1)

    if b:
        if maxi  <= k:
            k = maxi
        elif mini <=k:
            k = mini
        else:
            b = False


if b:
    print('YES')
else:
    print('NO')