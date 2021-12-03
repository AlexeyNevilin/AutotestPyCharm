'''import time
def function_time():
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
    print(f'Функция {ticket} выполнялась')


@function_time'''


import time
from datetime import datetime
def simple_decor(func):
    def func_time():
        data_start = datetime.now()
        print('Функция начала работу')
        func()
        print('Конец работы функции', '\n', 'Функция работала:', datetime.now() - data_start, 'сек.')
    return func_time

@simple_decor
def ticket():
    quantity = 0
    for i in range(1000000):
        i = str(i).zfill(6)
        if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5]):
            quantity += 1
    print(quantity)
