def sum_didgit(a):
    summ = 0
    for i in range(len(a)):
        summ += int(a[i])

    print(f'Сумма чисел: {summ}\n'
          f'Количество цифр в числе: {len(a)}\n'
          f'Разность суммы и количества цифр: {summ-len(a)}')



def del_digit(a):
    for i in range(2, a+1):
        if a%i == 0:
            print (i)
            break


sum_didgit((input('Ведите число: ')))
del_digit(int(input('Введите число: ')))
