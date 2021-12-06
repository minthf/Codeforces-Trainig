semen, antisemen, rocks = map(int, input().split())

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a        
    return a

while True:
    if rocks < gcd(semen, rocks):
        print(1)
        break
    rocks -= gcd(semen, rocks)
    if rocks < gcd(antisemen, rocks):
        print(0)
        break
    rocks -= gcd(antisemen, rocks)
