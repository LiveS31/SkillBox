#'Задача 1. Тестовое задание'
# f = 0
# for _ in range(6):
#     for i in range (f, 11 + f, 2):
#         print (i, end=' ')
#     f += 1
#     print()

#'Задача 2. Лестница'
# f, a = 0, int(input('Введите число:'))
# while f - 1 != a:
#     for _ in range(f):
#         print (f, end = ' ')
#     print()
#     f += 1

#'Задача 3. Рамка'
# x, y = int(input('ширена')), int(input('высота'))
# print('-'*x)
# for i in range(y):
#     print(f'|{" "*(x-2)}|')
# print('-'*x)

#Задача 4. Простые числа'
# w = 0
# for _ in range(int(input('Введите кол-во чисел:'))):
#     x, y = int(input('введите число:')), 0
#     for i in range(1,x+1):
#         u = x % i
#         if u == 0:
#             y += 1
#     if y == 2:
#         w += 1
# print ( 'Количество простых чисел в последовательности:', w)

#'Задача 5. Наибольшая сумма цифр# w = 0
# for _ in range(int(input('Введите кол-во чисел:'))):
#     x, y = int(input('введите число:')), 0
#     for i in range(1,x+1):
#         u = x % i
#         if u == 0:
#             y += 1
#     if y == 2:
#         w += 1
# print ( 'Количество простых чисел в последовательности:', w)

#'Задача 5. Наибольшая сумма цифр'

# c = []
# for _ in range(int(input('Количество цифр: '))):
#     c.append(int(input('Введите число:')))
# a = sum(map(int, str(c[0])))
# b = c[0]
# for i in c:
#     if sum(map(int, str(i))) > a:
#         a = sum(map(int, str(i)))
#         b = i
# print (f'Максимальное число: {b}, сумма чисел {a}')

#'Задача 6. Пирамидка'
a = int(input('Введите количество строк:'))
for i in range(a):
    print (' ' * (a-i-1) +  '#' * (i*2+1))

#'Задача 7. Пирамидка 2'
# a, b = int(input('Введите количество уровней:')), 1
# for i in range(1, a+1):
#   print('\t' * (a - i), end='')
#   for _ in range(i):
#     print(b, end='')
#     b += 2
#     print('\t' * 2, end='')
#   print('')

#'Задача 8. Яма '
# for i in range(1, (n := int(input())) + 1):
#      s = ''
#      for j in range(n, n - i, -1):
#           s += str(j)
#      print(s + '.' * (n * 2 - i * 2) + s[::-1])
