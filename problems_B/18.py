n = int(input())
s = list(map(int, input().split()))
banki = sorted(s)[::-1]

result = 0

for i in range(n):
    result += i * banki[i] + 1

print(result)

for i in range(n):
    print(s.index(banki[i]) + 1, end=' ')
    s[s.index(banki[i])] = -1

print('')


