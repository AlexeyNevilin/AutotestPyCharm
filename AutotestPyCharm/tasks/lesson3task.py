#Написать функцию cash, где аргументы deposit – сумма вклада, persent – процент  годовых, years – срок вклада.
#Функция возвращает сумму, которая будет к указанному году
def cash(deposit, persent, years): #Пример для ввода: cash(55000, 10, 20), сумма, ставка, количество лет
    for i in range(years):
        deposit += deposit / 100 * persent
    return round(deposit, 2)


#Напишите функцию, которая проверяет является ли число палиндромом
def palindrome(number): #Пример для ввода: palindrome(48984)
    number = str(number)
    if number == number[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')


#Вывести список простых чисел до 1000.
def prime_number(numb): #Пример для ввода: prime_number(50)
    list_numb = []
    for i in range(2, numb + 1):
        for s in range(2, i):
            if i % s == 0:
                break
        else:
            list_numb.append(i)
    return list_numb


#Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов.
#Билеты начинаются с 000000 и заканчиваются 999999.
#Счастливым считается билет, если сумма первых трех значений, равна сумме вторых трёх
''' ticket() '''
def ticket(): #Пример для ввода: ticket()
    quantity = 0
    for i in range(1000000):
        i = str(i).zfill(6)
        if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5]):
            quantity += 1
    return quantity


# Напишите функцию. На вход подается строка (текст), на выходе должен быть словарь, где ключ – это слово, а значение – число:
# сколько раз данное слово повторилось в тексте (регистр не имеет значения)

#Пример для ввода: charactersCount('Мело, мело по всей земле Во все пределы. Свеча горела на столе, Свеча горела. Метель лепила на стекле Кружки и стрелы. Свеча горела на столе, Свеча горела')
def charactersCount(text):
    text = text.title().replace('\n', ' ')
    sings = [',', '.']
    for i in sings:
        text = text.replace(i, '')
    list_word = text.split(' ')
    statistics = {s: list_word.count(s) for s in list_word if s}
    return statistics