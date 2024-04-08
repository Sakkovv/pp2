def true_check(f):
    return all(f)

p1 = input("Введите значение кортежей через пробелы: ")
p2 = p1.split()

p3 = tuple(bool(value) for value in p2)

p4 = true_check(p3)

if p4:
    print("Кортежи истины.")
else:
    print("Не все кортежи истины.")