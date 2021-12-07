vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
quesion = input()[:-1].split()
if quesion[-1][-1].upper() in vowels:
    print('YES')
else:
    print('NO')
