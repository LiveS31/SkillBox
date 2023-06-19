print('Задача 1. Урок информатики 2')
# x = float(input('Введите число:'))
# n = 0
# if x < 1:
#     while x < 1:
#         x *= 10
#         n -= 1
# elif x >= 10:
#     while x >= 10:
#         x /= 10
#         n += 1
# print(f'Формат плавающей точки: x = {round(x, abs(n))} * 10 ** {n}')

print('Задача 2. Функция максимума')
def maximum_of_three(a, b, c):
    if a > b or a == b:
        d = a
    else:
        d = b
    return maximum_of_two(d, c)
def maximum_of_two(d, c):
    if d > c or d == c:
        a = d
    else:
        a = c
    return a

print(maximum_of_three(int(input('a: ')), int(input('b: ')), int(input('c: '))))

#
# Здравствуйте, Сергей.
#
# 2 задание: функция принимает три числа и возвращает одно (наибольшее из трёх);
# при этом она должна использовать для сравнений первую функцию maximum_of_two. - эти условия не выполнены
#
# maximum_of_two наоборот, у вас принимает 3 аргумента
#
# return print(a) - плохая запись. Лучше вернуть число через return a
#
# а в основном коде записать уже вызов принта print(maximum_of_three(1, 2, 3))
#
# def maximum_of_three(a, b, c):
#     return a
#
#
# print(maximum_of_three(1, 2, 3))

print('Задача 3. Число наоборот 2')
# def reversal(a, b):
#     c = a[::-1]
#     d = b[::-1]
#     print(f'Первое число наоборот: {c}\n'
#           f'Второе число наоборот: {d}')
#     f = int(c)+int(d)
#     print (f'Сумма:  {f}\n'
#            f'Сумма наоборот: {str(f)[::-1]}')
#
# reversal(input('Введите первое число:'), input('Введите второе число:'))




print('Задача 4. Недоделка 2')
# def counting_digits(num):
#     count_ = 0
#     while num > 0:
#         count_ += 1
#         num //= 10
#     return count_
#
# def count_numbers(num_1):
#     temp = num_1
#     n = 1
#     last = num_1 % 10
#     temp //= 10
#     while temp:
#         first = temp % 10
#         temp //= 10
#         n *= 10
#     middle = num_1 % (first * n) // 10
#     return (last * n + middle * 10 + first)
#
# def main():
#     while True:
#         num_1 = int(input('Введите первое число: '))
#         if counting_digits(num_1) < 3:
#             print("В первом числе меньше трёх цифр.")
#         num_2 = int(input('Введите второе число: '))
#         if counting_digits(num_2) > 3:
#             num1, num2 = count_numbers(num_1), count_numbers(num_2)
#             print(f'Изменённое первое число: {num1}\n'
#                   f'Изменённое второе число: {num2}')
#             print(f'Сумма чисел {num2+num1}')
#             break
#         print("Во втором числе меньше четырёх цифр.")
# main()

print('Задача 5. Маятник ')

# amp = float(input('Введите начальную амплитуду: '))
# stp = float(input('Введите амплитуду остановки: '))
# n = 0
# d = 8.4/100
# while amp > stp:
#     amp *= 1-d
#     n += 1
# print(f'Маятник считается остановившимся через {n} колебаний')

print('Задача 6. Яйца')


# def formula(x):
#     return x ** 3 - 3 * x ** 2 - 12 * x + 10
# def calculate_safe_depth(danger_lvl):
#     min_depth = 0
#     max_depth = 4
#     result = (min_depth + max_depth) / 2
#     while abs(formula(result)) >= danger_lvl:
#         if abs(formula(min_depth)) < abs(formula(max_depth)):
#             max_depth = result
#         else:
#             min_depth = result
#         result = (min_depth + max_depth) / 2
#     return result
#
# def main_function(accept_danger_lvl):
#     result = calculate_safe_depth(accept_danger_lvl)
#     print(f'Приблизительная глубина безопасной кладки: {result} м')
#
# main_function(float(input('Введите максимально допустимый уровень опасности: ')))
