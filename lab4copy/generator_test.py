def generate_cube(n):
    for i in range(1, n+1):
        cube = i**3
        if cube <= n:
            yield cube

a = int(input())
b = generate_cube(a)
for j in b:
    print(j)



