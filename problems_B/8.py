n = int(input())

for i in range(n):
    s = int(input())
    print(len(set(list(map(int,input().split())))))
