def troich(x):
    res = ''
    while x:
        res += str(x % 3)
        x //= 3
    return res[::-1]



a, c = map(int, input().split())

at = troich(a)
ct = troich(c)

zeros = max(len(at), len(ct)) - min(len(at), len(ct))


if len(ct) > len(at):
    at = zeros * '0' + at

elif len(at) > len(ct):
    ct = zeros * '0' + ct
res = ''


for i in range(len(ct)):
    if int(ct[i]) < int(at[i]):
        res += str(int(ct[i]) + 3 - int(at[i]))
    else:
        res += str(int(ct[i]) - int(at[i]))


result = 0
for i in range(len(res)):
    result += int(res[-i - 1]) * (3 ** i)

print(result) 