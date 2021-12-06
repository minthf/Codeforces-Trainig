guest = [x for x in input()]
owner = [x for x in input()]
letters = [x for x in input()]

names = sorted(guest + owner)
letters = sorted(letters)

if names == letters:
    print("YES")
else:
    print("NO")
