def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

try:
    n = int(input("Введите число N: "))
    even_generator = generate_even_numbers(n)
    even_list = list(even_generator)
    print(f"Четные числа от 0 до {n}: {even_list}")
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите целое число.")
