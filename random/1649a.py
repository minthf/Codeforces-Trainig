t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = 0
    zeros = arr.count(0)
    if zeros == 0:
        print(0)
    elif zeros == 1:
        print(2)
    else:
        first = arr.index(0)
        last = len(arr) - 1 - arr[::-1].index(0)
        print(last-first + 2)