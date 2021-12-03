a = float(input())
b = float(input())
c = input()
if b == 0 and c == 'mod' and c == '/' and c == 'div':
    print("Деление на 0!")
elif c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '/':
    print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    print(a // b)