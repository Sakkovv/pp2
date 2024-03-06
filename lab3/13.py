import random
a = str(input("What is your name: "))

print(f"Well, {a}, I am thinking of a number between 1 and 20.")

psw = ' '
for x in range(21):
    psw = (random.randint(1, 20))

print(psw)
