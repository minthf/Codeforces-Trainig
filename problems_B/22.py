n = int(input())
s = list(map(int, input().split()))
chet = [x for x in s if x % 2 == 0]
nechet = [x for x in s if x % 2 != 0]

if abs(len(chet) - len(nechet)) <= 1:
    print(0)

elif len(chet) > len(nechet):
    count = len(chet) - len(nechet)
    print(sum(sorted(chet)[:count - 1]))

elif len(chet) < len(nechet):
    count = len(nechet) - len(chet)
    print(sum(sorted(nechet)[:count - 1]))