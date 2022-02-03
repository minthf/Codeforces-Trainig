t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    odd =0
    even = 0
    found = True
    for i in range(n):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    if even % 2 != odd % 2:
        print('NO')
        found = False
    else:
        if odd % 2 == 0:
            print('YES')
            found = False
        else:
            for i in range(n):
                if found == False:
                    break
                for j in range(n):
                    if arr[i] % 2 != arr[j] % 2 and abs(arr[i] - arr[j]) == 1:
                        print('YES')
                        found = False
                        break

    if found:
        print('NO')
