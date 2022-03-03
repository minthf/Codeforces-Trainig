n, k = map(int, input().split())
arr = list(map(int, input().split()))
MOD = 998244353;
p = -1;
ans = 1;
sum = 0;
for i in range(n):
    if (arr[i] >= n - k + 1):
    
        if (p != -1):
            ans = ans * (i - p) % MOD;
        sum += arr[i];
        p = i;
    

print(sum, ans)