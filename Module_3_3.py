# *args **kwargs

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print()
print('Задача "Распаковка"')

print_params()                            # вызов без аргументов
print_params(b = 25)                      # вызов c новым параметром b
print_params(c = [1,2,3])                 # вызов c новым параметром c в виде списка

print()
values_list = [4.0, 'Sasha' , [2,0,2,4]]    # список
values_dict = {'a':1,'b':2,'c':3}           # словарь
values_dict2 = {'c':'Словарь2'}              # словарь 2
values_list_2 = [54.32, 'Строка' ]          # 2ой список

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
print_params(*values_list_2, **values_dict2)
