from bs4 import BeautifulSoup
import requests

r = requests.get('https://divar.ir/s/tehran')



soup = BeautifulSoup(r.text, 'html.parser')

all_ads = soup.find_all('a', {'class': 'kt-post-card'})

for item in all_ads:
    price_tag = item.find('div', {'class': 'kt-post-card__description'})
    if price_tag and price_tag.text == 'توافقی':
        print(item.find('div', {'class': 'kt-post-card__title'}).text)
