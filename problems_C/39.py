n, sx, sy = map(int, input().split())

ans = [[sx+1, sy, 0], [sx-1, sy, 0], [sx, sy+1, 0], [sx, sy-1, 0]]
for i in range(n):
    x, y = map(int, input().split())
    if((sx-1>=x) or(sx-1==x and sy==y)):
        ans[1][2] += 1
    if((sy-1)>=y or(sx==x and  sy-1==y)):
        ans[3][2] += 1
    if((sy+1)<=y or(sx==x and  sy+1==y)):
        ans[2][2] += 1
    if((sx+1)<=x or (sx+1==x and  sy==y)):
        ans[0][2] += 1

maxi = ans[0]
for i in ans:
    if i[2] > maxi[2]:
        maxi = i
print(maxi[2])
print(maxi[0], maxi[1])
