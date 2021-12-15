n = int(input())
drinks = list(map(int, input().split()))

print(format(sum(drinks)/(n*100)*100, ".12f"))
