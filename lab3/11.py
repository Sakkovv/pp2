def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

user_input = input("Введите слово или фразу: ")

result = is_palindrome(user_input)

if result:
    print("Это палиндром.")
else:
    print("Это не палиндром.")
