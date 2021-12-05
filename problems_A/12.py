n = int(input())

for i in range(n):
    length = int(input())
    arr = list(map(int, input().split()))
    arr = list(set(arr))
    if len(arr) == 1:
        print("YES")
    else:
        for i in range(len(arr)):
            if len(arr) == 1:
                print("YES")
                break
            try:
                arr.index(max(arr) - 1)
                del(arr[arr.index(max(arr))])
            except ValueError:
                print("NO")
                break
