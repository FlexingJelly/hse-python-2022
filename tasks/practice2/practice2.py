import random
from typing import Iterable

UNCULTURED_WORDS = ('kotleta', 'pirog')


def greet_user(name: str) -> str:
    """
    Генерирует приветственную фразу.
    Приветствие не может состоять только из одного имени пользователя.

    :param name: имя пользователя
    :return: приветствие
    """

    greeting = 'Hello, ' + name + '!'
    return greeting


def get_amount() -> float:
    """
    Генерируем случайную сумму на счете.

    Сумма:
    - в диапазоне от 100 до 1000000
    - float
    - не больше 2-х знаков после запятой

    :return: случайную сумму на счете
    """

    amount = random.randint(100, 1000000) + random.randint(0, 100)/100
    return amount


def is_phone_correct(phone_number: str) -> bool:
    """
    Функция проверяет, что номер телефона соответствует следующему формату:
    +7xxxxxxxxxx, где x - цифра от 0 до 9

    :param phone_number: предполагаемый номер телефона
    :return: буленовское значение - bool: True - если номер корректны,
                                          False - если номер некорректный
    """

    result = phone_number[1:].isdigit()
    if phone_number.find('+7') != 0:
        result = False
    if len(phone_number) != 12:
        result = False
    
    return result


def is_amount_correct(current_amount: float, transfer_amount: str) -> bool:
    """
    Проверяет возможность осуществления перевода.
    Перевод возможен если выполняется условие:
    - текущий счет (current_amount) больше или равен сумме перевода (transfer_amount)

    :param current_amount: текущий счет
    :param transfer_amount: сумма перевода
    :return: буленовское значение - bool: True - если перевод возможен,
                                          False - если денег недостаточно
    """

    if current_amount >= float(transfer_amount):
        result = True
    else:
            result = False

    return result


def moderate_text(text: str, uncultured_words: Iterable[str]) -> str:
    """
    Модерирует текст по следующим правилам.

    Требования к тексту:
    - Первая буква заглавная, остальные буквы только в нижнем регистре
    - отсутствую лишние пробелы
    - фильтруются 'опасные' символы: " ' (двойные и одинарные кавычки)
    - слова, перечисленные в переменной uncultured_words заменяются на аналогичное количество знаков #

    :param text: исходный текст
    :param uncultured_words: список запрещенных слов
    :return: текст, соответсвующий правилам
    """

    text = text.strip()
    result = text.lower()
    first_letter = result[0]
    first_letter = first_letter.upper()
    result = result[1:]
    result = first_letter + result
    result = result.replace('  ', ' ')
    result = result.replace('\'', '')
    result = result.replace('\"', '')
    result = result.replace(uncultured_words[0], '#######')
    result = result.replace(uncultured_words[1], '#####')
    return result


def create_request_for_loan(user_info: str) -> str:
    """
    Генерирует заявку на кредит на основе входящей строки.
    Формат входящий строки:
    
    Иванов,Петр,Сергеевич,01.01.1991,10000
    
    Что должны вернуть на ее основе:
    
    Фамилия: Иванов
    Имя: Петр
    Отчество: Сергеевич
    Дата рождения: 01.01.1991
    Запрошенная сумма: 10000
    
    :param user_info: строка с информацией о клиенте
    :return: текст кредитной заявки
    """

    point_location = user_info.find(',')
    result = 'Фамилия: ' + user_info[:point_location] + '\n'
    user_info = user_info[point_location + 1:]
    point_location = user_info.find(',')
    result = result + 'Имя: ' + user_info[:point_location] + '\n'
    user_info = user_info[point_location + 1:]
    point_location = user_info.find(',')
    result = result + 'Отчество: ' + user_info[:point_location] + '\n'
    user_info = user_info[point_location + 1:]
    point_location = user_info.find(',')
    result = result + 'Дата рождения: ' + user_info[:point_location] + '\n'
    user_info = user_info[point_location + 1:]
    result = result + 'Запрошенная сумма: ' + user_info

    return result
