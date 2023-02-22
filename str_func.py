def get_word_user():
    words_user = input("Введите предложение\n")
    words_upper = words_user.upper()
    return words_upper


print(get_word_user())
