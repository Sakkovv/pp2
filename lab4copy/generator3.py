def generate_divisible_by_3_and_4(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
a = int(input("Введите число N: "))
b = generate_divisible_by_3_and_4(a)
print(f"Числа делющиеся на 3 и на 4: {list(b)}")
