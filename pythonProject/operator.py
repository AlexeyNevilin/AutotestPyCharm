a = 1
while a:
    a = int(input())
    if a < 10:
        continue
    if a > 100:
        break
    print(a)