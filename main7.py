# Задача 1
def bank(n):
    count = 0
    for i in range(n):
        b = int(input('Ведите номер клиента:'))
        if b < 0:
            b *= (-1)
        if b%2 == 0:
            if b > 0:
                count +=1
    print ('Всего положительных клиентов',(count))
bank(10)


# Задача 2
def pay():
    bonus = 0
    for i in range(1,13):
        bonus += int(input(f'Введите зарплату за {i}-й месяц:'))
    print(f'Ваша средняя зарплата за год - {bonus/12}')
    print(f'Ваша средняя зарплата за год - {int(bonus / 12)} - если имелось ввиду целое число')
pay()

#Задача 3
def factory(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    print ('Факториал числа',n,'равен',x)
factory(int(input('Введите свое число:')))

# Задача 4
def student(a,b,c):
    f = max(a,b,c)
    if f == a:
        f = 'троишников'
    elif f == b:
        f = 'хорошистов'
    elif f == c:
        f = 'отличников'

    print (f'Сегодня больше {f}!!!')

student(int(input('введите количество оценок 3:')),int(input('введите количество оценок 4:')),int(input('введите количество оценок 5:')))

#Задача 5
def digit(a,b):
    summ = 0
    cont = 0
    for i in range(a, b+1):
        g = i%3
        if g == 0:
            summ += i
            cont += 1
    print (summ//cont)

digit(int(input('Введите А')), int(input('Ведите В')))

#Задача 6
def chekdigit(digit):
    d = (digit//10) * (digit%10) * 3
    if d == digit:
        print(f'{d} - получившееся число равно оригиналу, значит число надо вывести')
    else:
        print('число выводить не нужно')
chekdigit(int(input('Введите число:')))

# задача 7
def card(n):
    a = []
    for i in range(1, n+1):
        a.append(i)
    for _ in range(1, n):
        b = int(input('Введите номера оставшихся карт:'))
        if b in a:
            a.remove(b)
    print ('Номер пропавшей карточки:',*a)

card(int(input('введите количество карточек:')))
