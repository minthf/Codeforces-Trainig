n = int(input())
for i in range(n):
    s = int(input())
    l = sorted(list(map(int, input().split())))
    print(l[s] - l[s-1])
