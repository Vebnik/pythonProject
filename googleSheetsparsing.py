from bs4 import BeautifulSoup
import requests

# Ссылка на удалённый ресурс с таблицей.
response = requests.get()

soup = BeautifulSoup(response.text, 'html.parser')

time_table_event = soup.find_all('tbody')

for time in time_table_event:
    #if(time == time.find_all('td', {'class':'s8'})):
    #    continue
    time = time.find_all('td', {'class':'s31'})
    print(time)

#print(time_table_event)
