import time
import math

n = float(input("Введите число: "))
ml = int(input("Введите время задержки(в миллисекундах) "))

time.sleep(ml/1000.0)
sqrt = math.sqrt(n)
print(f"Квадратный корень из {n} после {ml} миллисекунд: {sqrt}")