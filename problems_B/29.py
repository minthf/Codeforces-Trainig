n = int(input())
s = input()
delit = []

for i in range(1, n+1):
    if n % i == 0:
        delit.append(i)

for i in delit:
    s = s[0:i][::-1] + s[i:]
print(s)