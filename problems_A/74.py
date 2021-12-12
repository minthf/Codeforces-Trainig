n, m = map(int, input().split())

arr = []
count = 0 
for i in range(n):
    if i % 2 == 0:
        arr.append(['#' for x in range(m)])
    else:
        if count % 2 == 0:
            arr.append(['.' for x in range(m - 1)] + ['#'])    
        else:
            arr.append(['#'] + ['.' for x in range(m - 1)])
        count += 1


for i in arr:
    for k in i:
        print(k, end='')
    print('')
