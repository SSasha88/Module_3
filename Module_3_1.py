calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    return 'Длина этой строки:', len(string),'Верхний регистр:',string.upper(), 'Нижний регистр:', string.lower() # ринимает аргумент - строку и возвращает кортеж из:
    # длины этой строки, строку в верхнем регистре, строку в нижнем регистре.

def is_contains(string, list_to_search):
    count_calls()
    list = [item.lower() for item in list_to_search] # Функция is_contains принимает два аргумента:
    # строку и список, и возвращает True, если строка находится в этом списке,
    # False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    return string.lower() in list


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('UrBaN', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print('Счётчик вызовов: ', calls)
