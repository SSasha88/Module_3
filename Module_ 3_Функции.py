# int()  --> int(input())
# float()    число с плавающей точкой
# bool()    логические значения True (истина) и False (ложь)
# str()    используется для преобразования значения в строковый формат
# list()   списки, это упорядоченный набор элементов, каждый из которых имеет свой номер, или индекс,
# tuple()  Кортежи (тип tuple) — это неизменяемый тип данных в Python, который используется
           # для хранения упорядоченной последовательности элементов
# dict() Методы словарей · dict.clear() - очищает словарь. · dict.copy() - возвращает копию словаря. · dict.get(key[,
              # #default]) - возвращает значение ключа
# set()  множества

# dir(). Эта функция позволяет получить информацию об атрибутах объекта.

salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
print(round(sum(salary)/len(salary), 2), ' - средняя зарплата в компании')
print(round(max(salary), 2), ' - максимальная зарплата в компании')
print(round(min(salary), 2), ' - минимальная зарплата в компании')

names = ['Денис', 'Антон', 'Егор', 'Катя', 'Женя']
zipped = dict(zip(names, salary))
print(zipped['Денис'], '- зарплата Дениса')

                                                #ПРИМЕРЫ

# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список

def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_

print('# Максимум в списке', find_max([1, 2, 1, 5, 0]))

def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:
            continue
        if i % 2 == 0:
            counter += 1
    return counter

print('# Подсчёт четных чисел в списке',count_even([2, 2, 3, 4, 2, 1, 0]))

def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list

print('Уникальный список',unique([1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8]))

