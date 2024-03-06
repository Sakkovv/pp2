import math

def degree_to_radian(degree):
    radian = degree * (math.pi/180)
    return radian

a = int(input())
b = degree_to_radian(a)
print(f"из градуса в радиан: {b}")