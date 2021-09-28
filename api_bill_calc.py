import requests
import json
import time


# Беру ID У для подставления в DATA запроса
id_std = input('ID У: ')
print('-'*70)


# переменные цикла
qwert = 0
i = 0
id_serv = 0
i2 = 0
id_stk = 0
print_bal = 0


# Пустые списки для разных начислений
list_class = []
list_buy = []
list_2x2 = []
list_first = []
list_add_les = []
list_event = []
list_school = []
list_teacher = []
list_loyalty = []
list_payback = []
list_transfer = []
list_add_to_balance = []
list_convertion = []
list_compensation_other = []


# Пустые списки для СТК и общих уроков
list_his = []
list_stk_current = []
list_stk_bal = []
list_balance = []


# Данные для запроса к апи
url1 = '#'
url = '#'
params1 = json.dumps({'#'})
params = json.dumps({'#'})
headers = {'#'}


# Делаю запросы с к апи и получаю ответ в json
response_balance = requests.post(url, headers=headers, data=params1)
response_history = requests.post(url1, headers=headers, data=params)
res_bal = response_balance.json()
res_his = response_history.json()
time.sleep(1)


# Цикл - выделяю СТК услуг из массива
for pars in res_his['data']:
    list_stk_current.append(pars['serviceTypeKey'])
time.sleep(1)


# Вывожу список СТК для выобра
try:
    while qwert in range(len(set(list_stk_current))+1):
        print(i, list((set(list_stk_current)))[i])
        i += 1
        time.sleep(1)
except:
    print('-'*70)
id_service = int(input('ID Услуги: '))
print('-'*70)


# Прохожусь по массиву с ветвлением и условием по СТК и операции
for pars in res_his['data']:
    if pars['operation'] == 'class' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_class.append(pars['count'])
    elif pars['operation'] == 'buy' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_buy.append(pars['count'])
    elif pars['operation'] == '2x2' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_2x2.append(pars['count'])
    elif pars['operation'] == 'first_payment_auto_charge' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_first.append(pars['count'])
    elif pars['operation'] == 'add_lessons_by_promocode' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_add_les.append(pars['count'])
    elif pars['operation'] == 'event' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_event.append(pars['count'])
    elif pars['operation'] == 'compensation_school_error' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_school.append(pars['count'])
    elif pars['operation'] == 'compensation_teacher_miss_lesson' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_teacher.append(pars['count'])
    elif pars['operation'] == 'loyalty' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_loyalty.append(pars['count'])
    elif pars['operation'] == 'payback' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_payback.append(pars['count'])
    elif pars['operation'] == 'transfer' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_transfer.append(pars['count'])
    elif pars['operation'] == 'add_to_balance' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_add_to_balance.append(pars['count'])
    elif pars['operation'] == 'convertion' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_convertion.append(pars['count'])
    elif pars['operation'] == 'compensation_other' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_compensation_other.append(pars['count'])


# Отельный цикл по массиву, выделяю уроки, которые не были списаны, как пройденные.
for pars in res_his['data']:
    if pars['operation'] != 'class' and pars['serviceTypeKey'] == list(set(list_stk_current))[id_service]:
        list_his.append(pars['count'])


# Отдельно цикл по балансу, тут беру СТК из массива другого запроса.
for stk_bal in res_bal['data']:
    list_stk_bal.append(stk_bal['serviceTypeKey'])


# По длине списка с СТК задаю range и по СТК беру count
try:
    while i2 in range(len(set(list_stk_bal))):
        for pars_bal in res_bal['data']:
            if pars_bal['serviceTypeKey'] == list(set(list_stk_bal))[id_serv]:
                list_balance.append(pars_bal['count'])
        id_serv += 1
except:
    print('', end='')


# Вывожу все данные по У и подсчитываю кол-во уроков.
try:
    print('class: ', len(list_class))
    print('buy: ', list_buy)
    print('2х2: ', list_2x2)
    print('event: ', list_event)
    print('first_payment_auto_charge: ', list_first)
    print('add_lessons_by_promocode: ', list_add_les)
    print('compensation_school_error: ', list_school)
    print('compensation_teacher_miss_lesson: ', list_teacher)
    print('loyalty: ', list_loyalty)
    print('payback: ', list_payback)
    print('transfer: ', list_transfer)
    print('add_to_balance: ', list_add_to_balance)
    print('convertion: ', list_convertion)
    print('compensation_other: ', list_compensation_other)
    print('Всего уроков было начисленно: ', list_his, '=', sum(list_his))
    print('Всего уроков осталось: ', sum(list_his) - len(list_class))
    print('-' * 70)
    print('Количество уроков на всех услугах')
    while print_bal in range(len(set(list_stk_bal))):
        print(list(set(list_stk_bal))[id_stk], ':', list_balance[id_stk])
        id_stk += 1
    print(list(set(list_stk_current)))
except:
    print('')

