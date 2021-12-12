red, blue = map(int, input().split())

if red < blue:
    print(red, end=' ')
    blue -= red
    red = 0
elif red > blue:
    print(blue, end=' ')
    red -= blue
    blue = 0
else:
    print(red, end=' ')
    red = 0
    blue = 0

print(max(red, blue)//2)
