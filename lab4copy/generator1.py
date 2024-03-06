def generate_square(n):
    for i in range(1, n+1):
        square = i**2
        if square <= n:
            yield square

a = int(input("Введите число N: "))
b = generate_square(a)
print(f"Квадраты чисел до {a}: {list(b)}")