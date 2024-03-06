def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

user_input = input("Введите массив чисел, разделенных пробелами: ")
numbers = [int(num) for num in user_input.split()]

result = has_33(numbers)
print(result)
