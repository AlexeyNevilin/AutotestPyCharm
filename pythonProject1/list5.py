# Решено через ещё не изученную SUM
a = [int(i) for i in input().split()]
b = sum(a)
print(b)

# Как надо было решать
a = 0
for i in input().split():
    a += int(i)
print(a)