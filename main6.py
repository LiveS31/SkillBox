#задача 1
def up3(digit):
    for i in range(1,digit+1):
        print (i**3, sep=',')
#up3(int(input('Введите число: ')))

#Задача 2
def crimin():
    donat = 0
    while donat < 100:
        print('Василий, ваша задолженность составляет 100 рублей.')
        donat = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?'))
        if donat <100:
            print('Маловато, Василий. Давайте ещё раз.\n')
        else:
            print('Отлично, Василий! Вы погасили долг. Спасибо!')
            break
#crimin()
#Задача 3
def did_sum(didgital):
    print('Ответ:',len(didgital))
#did_sum(input('Введите число:'))

# Задача 4
def poznev():
    n = 1
    np = 0
    nn = 0
    while n != 0:
        n = int(input('Введите число:'))
        if n == 0:
            print('Кол-во положительных чисел:',np)
            print('Кол-во отрицательных чисел:',nn)
            break
        elif n >0:
            np +=1
        elif n < 0:
            nn += 1
#poznev()

#задача 5
def job():
    print("Начался 8-часовой рабочий день")
    jobs = 0
    wife = 0
    for i in range(8):
        jobs += int(input('Сколько задач решит Максим?'))
        wife += int(input('Звонит жена. Взять трубку? (1-да, 0-Нет'))
        print()
    print('Рабочий день закончился. Всего выполнено задач:',jobs)
    if wife >0:
        print('Нужно зайти в магазин')
#job()

#Задача 6
def bank(x, y, p):
    g = 0
    while x <= y:
        x += (x*p)
        g += 1
    if g >  int(g):
        g  += 1
    print ('Пройдет лет всего:',int(g), 'до получения желаемой суммы')

bank(int(input('Вклад:')), int(input('Желаемая сумма:')),
     int(input('Ставка банка годовых процентов:'))/100)



#Задача 7
def game(x):
    n = x+1
    num = 0
    while x != n:
        n = int(input('Введите число:'))
        num +=1
        if n > x:
            print ('Число больше, чем нужно. Попробуйте ещё раз!')
        elif n < x:
            print('Число меньше, чем нужно. Попробуйте ещё раз!')
    print('Вы угадали! Число попыток:',num)

#game(int(input('Введи число, которое нужно угадать:')))

#Задача 8

def gamecomp():
    a, b = 0, 0
    n, nn = 1, 100
    while 1 != a:
        b += 1
        x = (n+nn)//2
        a = int(input(f'Твое число: \n1 - равно\n2 - больше\n3 - меньше\nчисла {x}? '))
        if a == 2:
            n = x
        else:
            nn = x
    print (f'Это число - {x}\nУгадано за {b} попыток')


#gamecomp()


