n = int(input())
MOD = 1e9+7
res = 1
fact = 1
for i in range(1, n):
    res *= 2
    fact *= i
    fact %= MOD
    res %= MOD

fact *= n
fact %= MOD
fact -= res
fact %= MOD
if(fact < 0):
    fact += MOD
print(int(fact))