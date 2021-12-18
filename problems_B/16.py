n = int(input())

for i in range(n):
    a, b = map(int, input().split())

    candy = a // b * b
    a -= candy
    if a > (b // 2):
        candy += b // 2
    else:
        candy += a 
    print(candy)
