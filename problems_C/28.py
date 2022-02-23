n = int(input())
arr = list(map(int, input().split()))

i = 0
j = n - 1
left = 0
right = 0
ans = 0
while i < j + 2:
    if left < right:
        left += arr[i]
        i += 1
    elif left > right:
        right += arr[j]
        j -= 1
    else:
        ans = left
        right += arr[j]
        left += arr[i]
        j -= 1
        i += 1
print(ans)