a = int(input('Введите 1 число:'))
b = int(input('Введите 2 число:'))
max = 0
min = 0
print('1 Сложение',a+b)
print('2 Разность',a-b)
print('3 Произведение',a*b)
print('4 Среднее арифметическое',(a+b)/2)

if a<0:
    a = -1*a
if b<0:
    b = -1*b

if a>b:
    max = a
    min = b
elif b>a:
    max = b
    min = a 
else:
    max=a
    min=a
print('5 Разность максимума и минимума',max-min)
print('6 Частное',a/b)

