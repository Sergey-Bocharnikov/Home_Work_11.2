def get_word_user():
    """Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    words_user = input("Введите предложение\n")
    words_upper = words_user.upper()
    return words_upper


print(get_word_user())


def get_1word_user():
    """Функция, которая делает заглавными первые буквы каждого слова в строке"""
    words_user = input("Введите предложение\n")
    words_title = words_user.title()
    return words_title


print(get_1word_user())
