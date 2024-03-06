def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime():
    input_num = input("Введите числа, разделенные пробелами: ")
    numbers_list = [int(num) for num in input_num.split()]
    primes = list(filter(is_prime, numbers_list))
    return primes

result = filter_prime()
print("Простые числа:", result)
