simple = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
n, m = map(int, input().split())
if n not in simple or m not in simple:
    print('NO')
else:
    not_found = True
    for k, v in enumerate(simple):
        if n == v:
            not_found = False
            if m == simple[k+1]:
                print("YES")
            else:
                print('NO')
    if not_found:
        print("NO")
