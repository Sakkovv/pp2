def count_upper_and_lower(a):
    uppercase_count = sum(1 for char in a if char.isupper())
    lowercase_count = sum(1 for char in a if char.islower())
    return uppercase_count, lowercase_count


a = str(input("Введите строку: "))
uppercase, lowercase = count_upper_and_lower(a)
print("Количество прописных: ", uppercase)
print("Количество строчных: ", lowercase)