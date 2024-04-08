def V(v):
    v = 3/4 * 3.14 * n ** 2
    yield v 
n = int(input())
b = V(n)
for j in b:
    print(j)
