var = input()
'треугольник'
'прямоугольник'
'круг'
if var == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = ((a + b + c) / 2)
    S = ((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    print(S)
elif var == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = (a*b)
    print(S)
elif var == 'круг':
    r = float(input())
    S = ((r**2)*3.14)
    print(S)
