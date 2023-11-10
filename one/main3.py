def score(user):
    if user < 2:
        print('Ваш уровень: 1')
    elif 2 >= user <3:
        print('Ваш уровень: 2')
    elif 3 >= user <4:
        print('Ваш уровень: 3')
    else:
        print('Ваш уровень: 4')
# score(int(input())//1000)
def function(x):
    if x > 0:
        y = x-12
    elif x == 0:
        y = 5
    else:
        y = x**2
    print (f'Игрек равен: {y}')

#function(int(input('Введите икс:')))
def status(nubn, bal):
    if nubn >10:
        print ('К сожалению, вы не поступили.')
    elif nubn < 10 and bal < 290:
        print ('Поздравляем, Вы поступили!\nНо Вам не хватило баллов для стипендии')
    else:
        print ('Поздравляем, Вы поступили!\nБонусом Вам будет начисляться стипендия')
#status (int(input('Введите место в списке:')), int(input('Введите коллиичество балов за экамен:')))


# rating = int(input('Что получил по математике? '))
# if rating == 2 or rating == 3:
#     print('Плохо. Марш учиться!')
# if rating == 4 or rating == 5:
#     print('Молодец! Можешь отдохнуть.')

def digit(a, b, c):
    if a == b == c:
        print (3)
    elif a == b or b == c or c ==a:
        print (2)
    else:
        print (0)

#digit (int(input('Введите:\nчисло1: ')), int(input('число2: ')), int(input('число3: ')))

def kv(many, area):
    if many <= 10 and area >= 100:
        print ('Подходит, как первый вариант')
    elif many <= 7 and area >= 80:
        print('Подходит, как второй вариант')
    else:
        print ('Вариант не подходит')
#kv(int(input('Введите стоимость в млн:')), int(input('Введит площаь в м2:')))

def post(time):
    if 8 <= time < 10 or 12 <= time < 14 or 15 <= time < 18 or 20 <= time <22:
        print ('Можно получить посылку - способ 1')
    else:
        print( 'Посылку получить нельзя - способ 1')

    if time in (8, 9, 12, 13, 15, 16, 17, 20, 21):
        print ('Можно получить посылку - способ 2')
    else:
        print('Посылку получить нельзя - способ 2')


post(int(input('Введите интересующий Вас час: ')))

