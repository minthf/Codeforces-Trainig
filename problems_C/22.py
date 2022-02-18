n = int(input())
arr = sorted(list(map(int, input().split())))
ans = 0;
j = 0;
for i in range(n):
    while j < n and arr[j] - arr[i] <= 5:
        j += 1
        ans = max(ans, j - i);    

print(ans)