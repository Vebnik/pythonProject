# Аудит
sum1 = float(input('Сколько брал ивентов с аудита: '))
sum2 = float(input('Введи сумму аудита с нужного промежутка: '))

# Трекинг(Прод/общий)
# Время в переменной time3_1prod и time3_1obs будет использовано как основное с клокифай, так как конвертировано в еденицы часов.
time = float(input('Сколько часов в промежутке: '))
time3_prod = float(input('Сколько продуктивных часов в клокифай: '))
time3_1prod = float(input(('Сколько минут продуктивных в клокифай: '))) / 60 + time3_prod
time3_obs = float(input('Сколько часов общих в клокифай: '))
time3_1obs = float(input(('Сколько минут общих в клокифай: '))) / 60 + time3_obs


def track_prod_obs(x, y):
    a = (x / 100)
    b = (y / a)
    return b


def audit(x, y):
    su = x / (y/100)
    return su


print('--------------------------------------')
print('Аудит: ', audit(sum2,sum1), '%')
print('Трекинг продуктивный: ', track_prod_obs(time, time3_1prod), '%')
print('Трекинг общий: ', track_prod_obs(time, time3_1obs), '%')
print('--------------------------------------')