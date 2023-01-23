# Задача 1
def pay():
    bonus = 0
    for i in range(1,13):
        bonus += int(input(f'Введите зарплату за {i}-й месяц:'))
    print(f'Ваша средняя зарплата за год - {bonus / 12}')
#pay()

def factory(n):
    x = 1
    for i in range(1,n+1):
        x *= i
    print ('Факториал числа',n,'равен',x)
factory(int(input('Введите свое число:')))