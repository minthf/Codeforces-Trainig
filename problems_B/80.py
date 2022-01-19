n = int(input())
i =  2
s =  1
while n > 1:
    if n % i != 0:
        i += 1
    else:
        s += n
        n //= i
print(s)