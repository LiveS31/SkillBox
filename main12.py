# print('Задача 1. Сумма чисел')
# n = int(input('Введите число: '))
# print (f'Я знаю, что сумма чисел от 1 до {n} равна {sum([i for i in range(1, n + 1)])}')

#print('Задача 2. Функция в функции')

# n = int(input('Введите число: '))
# if n == 0:
#     print('Ноль не является ни отрицательным ни положительным целым числом')
# elif n > 0:
#     print ('Положительное')
# else:
#     print ('Отрицательное')

# print('======================================================================')
# print('Задача 3. Апгрейд калькулятора')
# while True:
#     print('Введите на первый запрос число для действий с ним, на второй действие:')
#     num1 = int(input('Введите: '))
#     num2 = int(input('Введите: '))
#     print(f'Сумма чисел - {(num1)+(num2)} ; Максимальная цифра числа - {max(num1,num2)}; Минимальная цифра числа - {min(num1,num2)}')

# print('Задача 4. Число наоборот')
# while True:
#     data = input('Введите число: ')
#     if data == '0':
#         print('Программа завершена!')
#         break
#     else:
#         print(f"Число наоборот: {(''.join(reversed([i for i in str(data)])))}")

# print('Задача 5. Текстовый редактор')
# def count_letters(*args):
#     K, N, text = args
#     return text.count(K), text.count(N)
# text = input('Введите текст: ')
# K = input('Какую цифру ищем? ')
# N = input('Какую букву ищём? ')
# answer = count_letters(K, N, text)
# print(f'Количество цифр {K}: {answer[0]}\nКоличество букв {N}: {answer[1]}')

# print('Задача 6. НОД')  #Напишите функцию, вычисляющую наибольший общий делитель двух чисел
# ЭТУ МАТЕШУ Я ПОМОГАТЬ НЕ БУДУ, ОНА МЕНЯ БЕСИТ И У МЕНЯ НОЧНЫЕ РАБОТЫ СКОРО
# def nod(a, b):
#     import math
#     return f'Наибольший общий делитель двух чисел - {math.gcd(a, b)}'
# a = int(input('Введите первое число - '))
# b = int(input('Введите второе число - '))
# print(nod(a, b))

# print('Задача 7. Недоделка')
def rock_paper_scissors():
    #Здесь будет игра "Камень, ножницы, бумага"
    from random import choice
    a = input('Введите камень, ножницы или бумага - ')
    b = choice(('камень', 'ножницы', 'бумага'))
    # print(a)
    print(f'Аппонент - {b}')
    if a == 'камень':
        if b == 'ножницы':
            print('Вы победили')
        elif b == 'бумага':
            print('Вы проиграли')
        else:
            print('Ничья')
    if a == 'ножницы':
        if b == 'камень':
            print('Вы проиграли')
        elif b == 'бумага':
            print('Вы победили')
        else:
            print('Ничья')
    if a == 'бумага':
        if b == 'ножницы':
            print('Вы проиграли')
        elif b == 'камень':
            print('Вы победили')
        else:
            print('Ничья')

def guess_the_number():
    #Здесь будет игра "Угадай число"
    from random import randrange
    while True:
        a = randrange(5)
        b = int(input('Нужно угадать число от 0 до 5, введите Ваш вариант - '))
        if a == b:
            print('Вы угадали')
            break
        else:
            print(f'Было загадано чило {a}, попробуйте еще раз')

def mainMenu():
    #Здесь главное меню игры
    print('Выберете игру:\nКамень, ножницы, бумага - 1\nУгадай число - 2\n')
    a = input('Введите 1 или 2 - ')
    if a == '1':
        rock_paper_scissors()
    else:
        guess_the_number()

mainMenu()