#Задача 1. Я стал новым пиратом!
# man = []
# for i in range(1, 2):
#     a = input(f'Человек {i} ведите слово:')
#     if a == "Карамба":
#         man.append(i)
# print ('Люди номер', *man, 'подходят')

#Задача 2. Кривой мессенджер
# text, a, b = input('Введите текст:'), 0, []
# for i in range(len(text)):
#     if text[i] == '*':
#         b.append(str(i+1))
# print(f'Символ «*» стоит на позиции', *b, sep=': ')

#Задача 3. Театр
# r, s, m = '', '=', '*'
# ry = int(input('Введите кол-во рядов:'))
# si = int(input('Введите кол-во ряду:'))
# me = int(input('Ведите кол-во метров между рядами:'))
# m *= me
# s *= si
# for i in range(ry):
#     print(s+' '+m+' '+s)

#Задача 4. Марсоход 2
# x, y, a = 8, 10, ''
# while a != 'q':
#     a = input(f'Марсоход находится на позиции {x}, {y}, введите команду:')
#     if a == 'w':
#         y +=1
#         if y>20:
#             y -=1
#             print('Препятствие')
#     elif a == 's':
#         y -= 1
#         if y <0:
#             y += 1
#             print('Препятствие')
#     elif a == 'a':
#         x -= 1
#         if x < 0:
#             x += 1
#             print('Препятствие')
#     elif a == 'd':
#         x += 1
#         if x > 15:
#             x -= 1
#             print('Препятствие')

#Задача 5. Великий и могучий
# a = 0
# for i in input('Введите текст:').strip('.').split():
#     if len(i)> a:
#         a = len(i)
# print (f'Самое длинное слово: {a} букв')

#Задача 6. Коровы
# a, b, c  = input('Введите стоила:'), -1, 0
# for i in range (2, 22, 2):
#     b +=1
#     if a[b] == 'b':
#         c +=i
# print('Всего литров молока:',c)

#Метод бутерброда
# a = 'shacnidw'
# print (a[::2]+a[1::2][::-1])
