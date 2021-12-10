n, c = map(int, input().split())

p = list(map(int, input().split()))
t = list(map(int, input().split()))

limak = 0
radewoosh = 0

time_l = 0
time_r = 0
for i in range(n):
    time_l += t[i]
    points = p[i] - (time_l * c)
    if points >= 0:
        limak += points

    time_r += t[- i - 1]
    points = p[- i - 1] - (time_r * c)
    if points >= 0:
        radewoosh += points

if limak > radewoosh:
    print('Limak')
elif limak < radewoosh:
    print('Radewoosh')
else:
    print('Tie')
