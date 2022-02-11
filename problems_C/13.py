n = int(input())
for i in range(n):
    t, k = map(int, input().split())
    print(k+((k-1)//(t-1)))