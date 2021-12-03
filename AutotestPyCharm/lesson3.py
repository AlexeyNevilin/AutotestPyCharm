"""def add(x, y):
    return x + y
print(add)

def func_without_args_and_returns():
    print('Печатаю этот текст и ничего не возвращаю')

a = func_without_args_and_returns()
print(a)"""


def my_func(a, b, c=2):
    d = (a + b) * c
    return d


print(my_func(1, 3))
print(my_func(1, 3, 4))
print(my_func(a=2, b=3))


# print(my_func(a = 2, c = 3)) будет ошибка так как не задано значение b

def list_is_default(a=[]):
    a.append(1)
    return a


print(list_is_default())
print(list_is_default())
print(list_is_default())
print(list_is_default())


# def first_default(a = None, b, c): у b и c тоже должеы быть указаны дефолтные значения
# return a, b, c

def func2(*args):
    return args


print(func2(1, 2.0, [3], 'abc'))
print(func2())
print(func2(15))

x = lambda a, b: a + b
print(x(3, 7))

s = lambda *args: args
print(s(1, 2.0, '3', [4]))
