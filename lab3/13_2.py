import random

def ygadaika():
    print("Привет! Я KBTU. Давай сыграем в игру в угадывание числа.")
    print("Я загадал число от 1 до 20.")

    number = random.randint(1, 20)
    attempt = 0

    while True:
        a = int(input("Угадай число: "))

        attempt += 1

        if a < number:
            print("Твоя догадка слишком низкая.")
        elif a > number:
            print("Твоя догадка слишком высокая.")
        else:
            print(f"Молодец, KBTU! Ты угадал мое число за {attempt} попыток!")
            break

if __name__ == "__main__":
    ygadaika()
