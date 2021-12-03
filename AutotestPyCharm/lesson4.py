#Нужно запускать через консоль
def simple_decor(fn):
    def wrapper():
        print('Сейчас запустится функция')
        fn()
        print('Функция отработала')
    return wrapper

@simple_decor
def some_func():
    print('Функция 1 работает')

@simple_decor
def some_func2():
    print('Теперь работает функция 2')


#Классы
class MyClass:
    pass
class Company:
    def __init__(self, name, director, structure):
        self.name = name
        self.director = director
        self. structure = structure
    def get_info(self):
        return f'Компания: {self.structure} {self.name}, Директор: {self.director}'
a = Company('Тензор', 'Уваров С.В.', 'ООО')
b = Company('РЖД', 'Белозеров О.В.', 'ОАО')
print(vars(a))
print(dir(a))
print(dir(Company))

def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x
print(fact(20))

def fibo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibo(n - 1) + fibo(n - 2)
print(fibo(7))
print(fibo(9))
print(fibo(20))
print(fibo(35))