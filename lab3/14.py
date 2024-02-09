def histogram(numbers=None):
    if numbers is None:
        print("histogram()")
        return

    for num in numbers:
        print('*' * num)


user_input = input("Введите массив чисел, разделенных пробелами: ")
numbers = [int(num) for num in user_input.split()]

histogram(numbers)
