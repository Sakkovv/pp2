import math
def calculate_polygon_area(sides, length):
    if sides < 3:
        return "polygon must have at least 3 sides."
    area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    
    return area

sides = int(input("Enter number of sides: "))

length = float(input("Enter the length of a side: "))

area = round(calculate_polygon_area(sides, length), 2)
print("area of the polygon is: ", area)
