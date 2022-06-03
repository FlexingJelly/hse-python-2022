from typing import Any, Optional


def search_phone(content: Any, name: str) -> Optional[str]:
    """
    Функция поиска номера телефона пользователя в структуре данных.

    Алгоритм работы следующий:
    1) принимаем на вход структуру content, состоящую из словарей,
    списков и строковых ключей в списке
    2) внутри структуры может быть запись следующего формата:
    {
        'name': 'user_name',
        'phone': 'user_phone',
    }

    3) необходимо пройтись по всей структуре
    4) если встречаем словарь, в котором ключ name совпадает с
    аргументом функции name - берем из этого словаря поле phone
    и возвращаем этот телефон из функции
    5) если поле name с таким значением не найдено - возвращаем из
    функции None

    Может пригодиться:

    1) Чтобы проверить, является ли объект списком используйте функцию:
    isinstance(some_object, list)
    если some_object список - результат будет True
    если some_object не список - False

    2) Чтобы проверить, является ли объект словарем используйте функцию:
    isinstance(some_object, dict)


    :param content: словарь или список, внутрь которого вложены объекты. Внутри
                      может скрываться номер телефона пользователя
    :param name: имя пользователя, у которого будем искать номер телефона
    :return: номер телефона пользователя или None
    """
    def check_values(content):
        checked_value = 0
        values_list = content.values()
        for value in values_list:
            print(value)
            if value == name:
                checked_value = values_list['phone']
        return checked_value

    def search_in_depth(data: Any, name: str):
        if isinstance(data, dict):
            searching_area = data.values()
        else:
            for part in data:
                list_search = search_in_depth(part, name)
                if list_search != 0:
                    return list_search
            return 0
        for part in searching_area:
            if part == None:
                return 0
            if part == name:
                return searching_area
            if not isinstance(part, int) and not isinstance(part, str):
                go_deeper = search_in_depth(part, name)
                if go_deeper != 0:
                    return go_deeper
        return 0
    phone_number = search_in_depth(content, name)
    if phone_number != 0:
        phone_number = str(phone_number)
        plus_place = phone_number.find('+')
        phone_number = phone_number[plus_place:]
        phone_number = phone_number[:12]
    else:
        return None



    return phone_number