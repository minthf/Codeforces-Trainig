n, m = map(int, input().split())
pixels = []
for i in range(n):
    pixels.append(input().split())

found = True

for i in pixels:
    if not found:
        break
    for k in i:
        if k not in ['B', 'W', 'G']:
            found = False
            print('#Color')
            break

if found:
    print('#Black&White')
