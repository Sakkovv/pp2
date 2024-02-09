def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

user_word = input("Введите предложение: ")
result = reverse_words(user_word)
print("Результат:", result)
