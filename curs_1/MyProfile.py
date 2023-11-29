import re

info_user = dict({
            'name': 'Отсутствует',
            'age': 'Отсутствует',
            'tel': 'Отсутствует',
            'mail': 'Отсутствует',
            'index': 'Отсутствует',
            'adress': 'Отсутствует',
            'info': 'Отсутствует',
            'ogrnip': 'Отсутствует',
            'inn': 'Отсутствует',
            'rs': 'Отсутствует',
            'bank': 'Отсутствует',
            'bik': 'Отсутствует',
            'kc': 'Отсутствует',
        })


def users_info_rec():
    vyb = input ('\nВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n'
               '1 - Личная информация\n'
               '2 - Информация о предпринимательстве\n'
               '0 - Назад\n'
               'Введите номер пункта меню: ')

    if '1' != vyb and '2' != vyb  and '0' != vyb:
        print('\033[31m\nВведены ошибочные данные!!!\nПовторите ввод!!!')
        return users_info_rec()

    elif vyb == '1':
        age = -1
        name = input('Имя: ')
        while int(age) < 0:
            age = input('Возраст: ')
            if not age.isdigit():
                print('\033[31mОшибка ввода! Повторите!')
                age = -1

        tel = ''
        while len(tel) < 11:
            for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Телефон в формате (+7XXXXXXXXXXX): ')))]:
                tel += i
            if len(tel) < 11:
                print('\033[31m\nОшибка вводам телефона!\nПовторите!!!!\n')
                tel = ''

        mail = ''
        while mail == '':
            mail = input('email: ')
            if '@' and '.' not in mail:
                print('\033[31m\nОшибка вводам eMail!\nПовторите!!!!\n')
                mail = ''

        index = ''
        while len(index) == 0 :
            for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Введите почтовый индекс: ')))]:
                index += i
            if len(index) == 0:
                print('\033[31m\nОшибка вводам индекса!\nПовторите!!!!\n')
                index = ''



        g = {
            'name': name,
            'age': age,
            'tel': '+'+tel,
            'mail': mail,
            'index': index,
            'adress': input('Введите почтовый адрес (без индекса): '),
            'info': input('Введите дополнительную информацию: ')
        }
        info_user.update(g)

    elif vyb == '2':
        b = ''
        while len(b) != 15:
            for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Введите ОГРНИП: ')))]:
                b += i
            if len(b) != 15:
                print('\033[31m\nОшибка ввода! Повторите!\n')
                b = ''

        inn = ''
        for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Введите ИНН: ')))]:
            inn += i

        rs = ''
        while len(rs) != 20:
            for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Введите К/с: ')))]:
                rs += i
            if len(rs) != 20:
                print('\033[31m\nОшибка ввода! Повторите!\n')
                rs = ''

        bank = input('Введите Банк: ')

        bik = ''
        for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Введите БИК: ')))]:
            bik += i

        kc = ''
        for i in [i for i in (re.findall(r'\d\.d+|\d+', input('Введите К/с: ')))]:
            kc += i

        g = {
            'ogrnip': b,
            'inn': inn,
            'rs': rs,
            'bank': bank,
            'bik': bik,
            'kc': kc,
        }
        info_user.update(g)

    else:
        return menu_global()
    return users_info_rec()


def menu_info_views():
    if not len(info_user):
        print ('\nПользователя не существует!!!!\n')
        return menu_global()
    vyb = input('\nВЫВЕСТИ ИНФОРМАЦИЮ\n'
          '1 - Общая информация\n'
          '2 - Вся информация\n'
          '0 - Назад\n'
          'Введите номер пункта меню: ')

    if '1' != vyb and '2' != vyb  and '0' != vyb:
        print('\033[31m\nВведены ошибочные данные!!!\nПовторите ввод!!!')
        return menu_info_views()
    elif not len(info_user):
        print ('Пользователя не существует!!!!')

    elif vyb == '1':
        print(f'Есть {len(info_user)} пользователь(ей).\nВыберите согласно номеру:\n')
        print(
            f"\nИмя:   {info_user['name']}\n"
            f"Возраст: {info_user['age']}\n"
            f"Телефон: {info_user['tel']}\n"
            f"E-mail:  {info_user['mail']}\n"
            f"Индекс:  {info_user['index']}\n"
            f"Адрес:   {info_user['adress']}\n"
            f"Дополнительная информация: {info_user['info']}\n"
        # про последний пункт не понял где его выводить.
        #     но так как это словарь - вписать это можно везде

        )
    elif vyb == '2':

        print(
            f"\nИмя:     {info_user['name']}\n"
            f"Возраст: {info_user['age']}\n"
            f"Телефон: {info_user['tel']}\n"
            f"E-mail:  {info_user['mail']}\n"
            f"Индекс:  {info_user['index']}\n"
            f"Адрес:   {info_user['adress']}\n"
            f"\nИнформация о предпринимателе\n"
            f"ОГРНИП:  {info_user['ogrnip']}\n"
            f"ИНН:     {info_user['inn']}\n"
            f"Банковские реквизиты\n"
            f"Р/с:     {info_user['rs']}\n"
            f"Банк:    {info_user['bank']}\n"
            f"БИК:     {info_user['bik']}\n"
            f"К/с:     {info_user['kc']}\n"

        )

    else:
        return menu_global()
    return menu_global()

def menu_global():
    print ('\033[34mПриложение MyProfile\nСохраните информацию о себе и выводите ее в разных форматах')
    print ('\033[32mГЛАВНОЕ МЕНЮ')
    print ('1 - Ввести или обновить информацию\n2 - Вывести информацию\n0 - Выход')
    vyb = input('\033[36mВведите номер пункта меню: ')
    if '1' != vyb and '2' != vyb  and '0' != vyb:
        print('\033[31mВведены ошибочные данные!!!\nПовторите ввод!!!')
        return menu_global()
    elif vyb == '1':
        return users_info_rec()
    elif vyb == '2':
        return menu_info_views()
    else:
        print('\033[30mПрограмма остановлена')
        return


if __name__ in '__main__':
    menu_global()