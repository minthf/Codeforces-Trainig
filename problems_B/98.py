s = input()
not_a = [x for x in s if x != 'a']
lenght = len(not_a)

if lenght % 2 != 0:
    print(':(')
elif not_a[lenght//2:] != not_a[:lenght//2] or s[len(s) - lenght//2:].count('a') > 0:
    print(':(')
else:
    if lenght == 0:
        print(s)
    else:
        print(s[:-lenght//2])
