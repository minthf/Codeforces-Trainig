import sys
input = sys.stdin.readline
 
t = int(input())
for _ in range (t):
    n = int(input())
    a = list(map(int, input().split()))
 
    if a.count(1) != 1:
        print("NO")
        continue
 
    a.append(a[0])
    ok = True
    for i in range (0, n):
        if a[i + 1] - a[i] > 1:
            ok = False
            break
    
    if ok: print("YES")
    else: print("NO")