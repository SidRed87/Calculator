print('Визначаємо слово поліндром')
a = str(input('Введіть будь-яке слово - '))
b = (a[::-1])

if a in b:
    print('True')
else:
    print('False')