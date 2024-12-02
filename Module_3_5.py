# Задача "Рекурсивное умножение цифр"

def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) == 1:
        return int(str_number)
    first = int(str_number[0])
    return first * get_multiplied_digits(int(str_number[1:]))

# Пример 1
result = get_multiplied_digits(40203)
print('Пример 1:', result)

# Пример 2
result2 = get_multiplied_digits(402030)
print('Пример 2:', result2)
