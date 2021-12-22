#Напишите функцию, которая подсчитывает количество счастливых шестизначных билетов.
#Билеты начинаются с 000000 и заканчиваются 999999.
#Счастливым считается билет, если сумма первых трех значений, равна сумме вторых трёх
def ticket():
    quantity = 0
    for i in range(1000000):
        i = str(i).zfill(6)
        if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5]):
            quantity += 1
    return quantity

'''d = 0
for i in range(999999 + 1):
    i = str(i).zfill(6)
    if int(i[0]) + int(i[1]) + int(i[2]) == int(i[3]) + int(i[4]) + int(i[5]):
        d += 1
print(d)'''
