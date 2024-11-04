import requests
import bs4 as BeautifulSoup
import json
url = 'https://www.mse.mk/mk/stats/symbolhistory/REPL'

response = requests.post(url, data = {
  'FromDate': '01.12.2023',
  'ToDate': '04.11.2024',
  'Code': 'REPL'
})

html = response.text
soup = BeautifulSoup.BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')


rows = table.find_all('tr')
dates = [row.find('td').text for row in rows]
values = [row.find('td', {'class': 'td-right'}).text for row in rows]

for date, value in zip(dates, values):
    print()
    print(f'Date: {date}, Value: {value}')
    print('-' * 10)
    print()

