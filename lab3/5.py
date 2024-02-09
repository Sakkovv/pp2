from itertools import permutations

def print_permutations(input_string):
    print("Перестановка строки:")
    for permuted_string in permutations(input_string):
        print(' '.join(permuted_string))

user_input = input("Введите строку: ")
print_permutations(user_input)
