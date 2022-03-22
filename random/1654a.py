t = int(input())
for i in range(t):
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print(arr[-1] + arr[-2])