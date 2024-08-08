def print_params(a=1, b='строка', c=True):
    print(a, b, c)
value_list = [2.5, 'Rabbit', (3, 4)]
values_dict = {'a': 1, 'b': 'муж', 'c': (10, 9, 8)}
values_list_2 = [54.32, 'Строка']
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(*value_list)
print_params(**values_dict)
print_params(*values_list_2, 42)





