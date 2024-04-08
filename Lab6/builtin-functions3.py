def palindrom(p):
    p = p.lower().replace(" ", "")
    return p == p[::-1]

p = input("Введите строку: ")

if palindrom(p):
    print("Палиндром")
else:
    print("Не палиндром")
