n = int(input())

for i in range(n):
    m = int(input())


    candy = list(map(int, input().split()))
    oranges = list(map(int, input().split()))
    min_candy = min(candy)
    min_oranges = min(oranges)
    count = 0
    tmp = 0
    tmp1 = 0
    for i in range(m):
        tmp = 0
        tmp1 = 0
        if candy[i] > min_candy:
            tmp = candy[i] - min_candy

        if oranges[i] > min_oranges:
            tmp1 = oranges[i] - min_oranges

        count += max(tmp, tmp1) 

    print(count)
