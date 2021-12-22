#Написать функцию cash, где аргументы deposit – сумма вклада, persent – процент  годовых, years – срок вклада.
#Функция возвращает сумму, которая будет к указанному году
def cash(deposit, persent, years):
    for i in range(years):
        deposit += deposit / 100 * persent
    return round(deposit, 2)

'''def cash(deposit, persent, years):
    return deposit + deposit * persent * years
print('Ожидаемая сумма по вкладу:', int(cash(10000, 0.07, 13)))'''