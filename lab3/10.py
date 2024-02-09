def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

user_input = input("Введите список чисел, разделенных пробелами: ")
input_list = [int(num) for num in user_input.split()]

result = unique_elements(input_list)

print("Исходный список:", input_list)
print("Список уникальных элементов:", result)
