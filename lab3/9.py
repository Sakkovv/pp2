import math

def volume_sphere(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

radius = float(input("Введите радиус сферы: "))
result = volume_sphere(radius)
print(f"Объем данной сферы составляет {result}")
