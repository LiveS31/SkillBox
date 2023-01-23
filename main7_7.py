# Задача 2
def pay():
    bonus = 0
    for i in range(1,13):
        bonus += int(input(f'Введите зарплату за {i}-й месяц:'))
    print(f'Ваша средняя зарплата за год - {bonus / 12}')
#pay()

#Задача 3
def factory(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    print ('Факториал числа',n,'равен',x)
#factory(int(input('Введите свое число:')))

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

#student(int(input('введите количество оценок 3:')),int(input('введите количество оценок 4:')),int(input('введите количество оценок 5:')))

#Задача 5
def digit(a,b):
    sum = 0
    cont = 0
    for i in range(a, b+1):
        g = i%3
        if g == 0:
            sum += i
            cont += 1
    print (sum//cont)

#digit(int(input('Введите А')), int(input('Ведите В')))

#Задача 6
def chekdigit(digit):
    d = (digit//10) * (digit%10) * 3
    if d == digit:
        print(f'{d} - получившееся число равно оригиналу, значит число надо вывести')
    else:
        print('число выводить не нужно')
chekdigit(int(input()))

# задача 7

