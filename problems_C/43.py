N = 50000
def check_prime(n):
    for i in range(2, min(N, n)):
        if n % i == 0:
            return 0
    return 1

t = int(input())
for i in range(t):
    n = int(input())

    lose = n == 1
    if n > 2 and n % 2 == 0:
        if ((n & (n - 1)) == 0):
            lose = 1
        elif (n % 4 != 0 and check_prime(n // 2)):
            lose = 1

    if(lose):
        print('FastestFinger')
    else:
        print('Ashishgup')
