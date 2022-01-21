import math
n = int(input())
groups = list(map(int, input().split()))
ones = groups.count(1)
twos = groups.count(2)
threes = groups.count(3)
fours = groups.count(4)

tmp = min(ones, threes)
res = tmp

ones -= tmp
threes -= tmp

tmp = twos // 2
res += tmp

twos -= tmp * 2

res += fours

if threes > 0:
    res += threes

if twos > 0:
    res += 1
    ones -= 2

if ones > 0: 
    res += math.ceil(ones/4)

print(res)
