a = input()
if a == a[::-1]:
    print('YES')
else:
    print('NO')

s = 'abcdefghijk'
print(s[3:6], s[:6], s[3:], s[::-1], s[-3:], s[:-6], s[-1:-10:-2])