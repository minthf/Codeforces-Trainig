n = int(input())
for i in range(n):
    s = input().split('R')
    maxi = len(max(s))
    print(maxi + 1)