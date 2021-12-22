# Напишите функцию. На вход подается строка (текст), на выходе должен быть словарь, где ключ – это слово, а значение – число:
# сколько раз данное слово повторилось в тексте (регистр не имеет значения)
''' charactersCount('Мело, мело по всей земле Во все пределы. Свеча горела на столе, Свеча горела. Метель лепила на стекле Кружки и стрелы. Свеча горела на столе, Свеча горела') '''
def charactersCount(text):
    text = text.title().replace('\n', ' ')
    sings = [',', '.']
    for i in sings:
        text = text.replace(i, '')
    list_word = text.split(' ')
    statistics = {s: list_word.count(s) for s in list_word if s}
    return statistics



'''import collections
def charactersCount(text):
    quantity = collections.Counter()
    for i in list(text.title().replace('.', ' ').replace(',', ' ').split()):
        quantity[i] += 1
    return quantity
print(dict(charactersCount('Мело, мело по всей земле Во все пределы. Свеча горела на столе, Свеча горела. Метель лепила на стекле Кружки и стрелы. Свеча горела на столе, Свеча горела')))'''

'''def string(**kwargs):
    # a = (Мело='2', Свеча='4', горела='4', на='3')
    # a = (Мело = '2', Свеча = '4', горела = '4', на = '3')
    return kwargs


print(string(Мело = '2', Свеча = '4', горела = '4', на = '3'))'''


