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
