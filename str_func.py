def get_word_user():
    "Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"
    words_user = input("Введите предложение\n")
    words_upper = words_user.upper()
    return words_upper


print(get_word_user())
