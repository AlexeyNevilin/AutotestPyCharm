number = str(input('Введите номер телефона: ').replace('-', '').replace('+', '').replace(' ', ''))
if number.isdigit():
    print('Номер состоит только из цифр')
else:
    print('Номер состоит не только из цифр')
