def square_of_number(a, b):
    for i in range(a, b +1):
        yield i ** 2

a = int(input())
b = int(input())
for square in square_of_number(a, b):
    print(square)