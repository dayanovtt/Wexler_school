def parametrize(*args, list_of_params):
    def _parametrize(f):
        def wrap(*args, **kwargs):
            for params in list_of_params:
                print(f'Вызываем функцию {f} с параметрами {params}')
                result = f(**params)
                print(f'Результат: {result}')
        return wrap
    return _parametrize

@parametrize(list_of_params=[{'a': 5, 'b': 10}, {'a': 6, 'b': 10}, {'a': 7, 'b': 1}])
def divide_two_numbers(a, b):
    return a / b

divide_two_numbers(5, 5)