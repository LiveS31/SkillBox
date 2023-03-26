# print('Задача 1. Конвертация')
# check = float(input ('Введитетстоимость покупки: '))
# s = 60.87
# es = 1.25
# # es= 1.25 = s =60.87
# print (f'Сумма в рублях: {(check*es)*s}')

# print('Задача 2. Грубая математика')
# import math
# for i in range (int(input('Введите колличество чисел:'))):
#     digital = float(input('Введите число: '))
#     if digital == 0:
#         print(digital)
#         break
#     elif digital > 0:
#         print (f'x = {math.ceil(digital)}  log(x)= {math.log((math.ceil(digital)))}')
#     else:
#         print(f'x= {math.floor(digital)}  exp(x) ={math.exp(math.floor(digital))}')

# print('Задача 3. Аналог Steam')
# import math
# size = int(input('Введите размер файла:'))
# speed = int(input('Введите скорость интернета:'))
# raz, temp = math.ceil(size/speed), 0
# for i in range (1,raz+1):
#     temp += speed
#     if temp < size:
#         print(f'Прошло {i} сек. Скачано {temp} из {size} Мб ({math.ceil(100*speed/(size))*i}%)')
#     elif temp >= size:
#         print(f'Прошло {i} сек. Скачано {size} из {size} Мб (100%)')


# print('Задача 4. Первая цифра')
# print(int(float(input())*10)%10)

# print('Задача 5. Вот это объёмы!')
# r = float(input('Введите радиус планеты: '))
# v = 10.8321 * (10 ** 11)
# vv = round(4 * 3.1415926535/3 * (r**3), 3)
# if vv < v:
#     print(f'Объём планеты Земля больше в {round(v/vv, 3)} раз')
# else:
#     temp =round(vv/v, 3)
#     print(f'Объём планеты Земля меньше в (1/{(str(round(1/temp, 3)))}) = {temp} раз')

# print('Задача 6. Ход конём')
# x = float(input('Введите местоположение коня x: '))
# y = float(input('Введите местоположение коня y: '))
# xstep = float(input('Введите местоположение точки на доске x: '))
# ystep = float(input('Введите местоположение точки на доске y: '))
# xhorse = int(x * 10)
# yhorse = int(y * 10)
# sxhorse = int(xstep * 10)
# syhorse = int(yhorse * 10)
# print(f'Конь в клетке ({xhorse}, {yhorse}). Точка в клетке ({sxhorse}, {syhorse}).')
# if abs((x-sxhorse) * (y-syhorse)) == 2:
#     print('Нет, конь не может ходить в эту точку.')
# else:
#     print('Да, конь может ходить в эту точку.')

# print('Задача 7. За что?')
# #?????
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print (f'Бодльшее число {int((a + b + abs(a - b)) / 2)}')

