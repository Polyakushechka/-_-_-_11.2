def foo1():
    """
    Функция для увеличения букв
    :return:
    """
    a = str(input())
    return a.capitalize()


def foo2():
    """
    Функция делает первые буквы слов заглавными
    :return:
    """
    b = str(input())
    words = b.split(" ")
    for word in words:
        return word[0].capitalize()