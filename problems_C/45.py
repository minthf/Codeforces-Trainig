t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    summary = sum(arr)
    xor = 0
    for i in arr:
        xor = xor ^ i
    print(2)
    print(xor, summary+xor)