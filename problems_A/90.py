n = int(input())
grani = 0
for i in range(n):
    s = input()
    if s == "Tetrahedron":
        grani += 4
    elif s == "Cube":
        grani += 6
    elif s == "Octahedron":
        grani += 8
    elif s == "Dodecahedron":
        grani += 12
    elif s == "Icosahedron":
        grani += 20

print(grani)
