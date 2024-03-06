def number_to_zero(n):
    while n >=0:
        yield n
        n -= 1

a = int(input())
for number in number_to_zero(a):
    print(number)