n = int(input())

for i in range(n):
    hp, void, light = map(int, input().split())

    for i in range(void):
        if hp <= 20:
            break
        hp = int((hp / 2) + 10)
        
    for i in range(light):
        hp -= 10

    if hp <= 0:
        print('YES')
    else:
        print('NO')
