# задача 1
# mes = 0
# for i in range(100, 0, -4):
#     print(f'{i} гречки будет в запасе через: {mes} мес.')
#     mes += 1

#Задача 2
# bad_man = int(input('Ввелите количество должников: '))
# summ = 0
# for i in range(0,bad_man, 5):
#     print (f'Должник с номером {i}')
#     summ += int(input('Сколько Вы должны?'))
# print (f'Общая сумма долга {summ}')

# Задача 3
# sec = int(input('Введите количество секунд:'))
# for i in range (sec , 0, -1):
#   print (f'Количество секунд: {i} cекунд')
#   reverse_timer = int(input('Вы готовы забрать еду? '))
#   if reverse_timer == 1:
#     print (f'Ваша еда готова, можно забрать {i} cекунд')
#     break
# print('Ваша еда готова, осторожно, горячо!')

# #Задача 4
# print ('Введите число')
# a, b, c = int(input('а')), int(input('b')), int(input('c'))
# if c == 0:
#     print ('ERROR!!!! c - не может быть 0')
# else:
#     summ, cont = 0, 0
#     for i in range (a, b+1):
#         if i % c == 0:
#             summ +=i
#             cont +=1
#     if cont != 0:
#         print(summ/cont)
#     else:
#         print ('НЕТ ЧИСЛА')

# задача 5
# a = int(input('Введите начало:'))
# b = int(input('Ведите конец:'))
# step = int(input('введите шаг:'))
# for x in range(b, a - 1, step):
#     print (f'В точке {x} функция равна: {x**3 + 2 *x**2 - 4*x + 1}')

# Задача 6
# paper_x = int(input('Введите размер квадратно листа:'))
# kol = 0
# while paper_x > 11.9: # тут я в замешательстве... ну в 12 письмо влезть не должно :)
#         kol += 1
# print(kol)

# задаче 7
# educational_grant = int(input('Введите степендию:'))
# expenses = int(input('Введите траты:'))
# for i in range(2, 1+10):
#         expenses += (expenses * 0.03)
# print (f'Взять денег у родителей: {round(expenses,2)-educational_grant} рубля' )

# Задача 8
# n = int(input('Введите число n: '))
# print('S =',(1.0 - (-0.5) ** (n + 1)) / 1.5)

# Задача 9
# x = int(input('Введите число x: '))
# a = 1
# b = 0
# j=1
# r=1
# for _ in range(6):
#     b += b+1
#     j *= (x-b)
# for _ in range(6):
#     a +=a
#     r *= (x-a)
# if b == 0:
#     print ("Ошибка! на 0 делить нельзя!")
# else:
#     print ('Значение выражения', j/r)



# #Задача 10 -----
x = int(input('Введите кол-во мальчиков:'))
y = int(input('Введите кол-во девочек:'))
ans =''
if (x > 2 * y) or (y > 2 * x):
    print('Нет решения')
elif x >= y:
    k = x - y
    for i in range(k):
        ans += 'BGB'
    for ii in range(y - k):
        ans += 'BG'
else:
    k = y - x
    for i in range(k):
        ans += 'GBG'
    for ii in range(x - k):
        ans += 'GB'
print(ans)

