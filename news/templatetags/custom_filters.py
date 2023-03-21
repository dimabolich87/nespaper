from django import template

register = template.Library()

censored_words = ['редиска']


# Регистрируем фильтр в библиотеке шаблонов с помощью декоратора
@register.filter()
def censor(value):
    if not isinstance(value, str):  # проверяем тип переменной
        raise ValueError("Фильтр работает только для строк")  # выбрасываем исключение, если тип переменной не строка

    words = value.split()  # разбиваем текст на слова
    for i, word in enumerate(words):
        if word.lower() in censored_words:  # если слово нужно заменить
            words[i] = '*' * len(word)  # заменяем слово на символ "*"
    return ' '.join(words)  # объединяем слова в строку и возвращаем результат

