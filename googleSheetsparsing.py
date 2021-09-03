from bs4 import BeautifulSoup
import requests

# Ссылка на удалённый ресурс с таблицей.
response = requests.get('Вот тут ссылка на таблицу в сети/удалённом сервера с постоянным обновлением')

soup = BeautifulSoup(response.text, 'html.parser')

time_table_event = soup.find_all('tbody')

for time in time_table_event:
    #if(time == time.find_all('td', {'class':'s8'})):
    #    continue
    time = time.find_all('td', {'class':'s31'})
    # Пока вывод на стороне консоли. Потом ответ будет улетать в БД под MySQL.
    print(time)

#print(time_table_event)
