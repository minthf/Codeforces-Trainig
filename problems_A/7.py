n, m = map(int, input().split())
arr = []
ogr = []
for i in range(n):
    arr.append(input())
    for k, v in enumerate(arr[i]):
        if v == '*':
            ogr.append([i, k])
if ogr[0][0] == ogr[1][0]:
    if ogr[0][1] == ogr[2][1]:
        print(ogr[2][0] + 1, ogr[1][1] + 1)
    else:
        print(ogr[2][0] + 1, ogr[0][1] + 1)
else:
    if ogr[0][1] == ogr[2][1]:
        print(ogr[0][0] + 1, ogr[1][1] + 1)
    else:
        print(ogr[0][0] + 1, ogr[2][1] + 1)

