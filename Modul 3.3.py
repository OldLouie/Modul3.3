def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()                                      # вызов фунции без аргументов
print_params('coconut', 20)                  # вызов функции с разным количеством аргументов
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, 'nuts', False]
values_dict = {'a': 1, 'b': 'строка', 'c': True}
print_params(*values_list)                          # распаковка параметров (* для списка).
print_params(**values_dict)                         # распаковка параметров (** для словаря).

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)