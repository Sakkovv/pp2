def spy_game(nums):
    spy_code = [0, 0, 7]
    
    for num in nums:
        if num == spy_code[0]:
            spy_code.pop(0)
        if not spy_code:
            return True
    return False

user_input = input("Введите массив чисел, разделенных пробелами: ")
numbers = [int(num) for num in user_input.split()]

result = spy_game(numbers)
print(result)
