from bs4 import BeautifulSoup
import requests
import mysql.connector
import re


conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='maktabkhooneh')
cursor = conn.cursor()

car_name = input("Enter car name: ").lower()

page = 1
count = 0
while count < 20:
    print('request page', str(page))
    r = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=' + str(page))

    soup = BeautifulSoup(r.text, 'html.parser')

    all_ads = soup.find_all('div', {'class': 'vehicle-card'})
    count_in_page = 0
    for item in all_ads:
        title_tag = item.find('span', {'class': 'vehicle-header-make-model'})
        model_tag = item.find('div', {'data-test': 'vehicleCardTrim'})
        
        if (title_tag and car_name in title_tag.text.lower()) or (model_tag and car_name in model_tag.text.lower()):
            mileage = item.find('div', {'data-test': 'vehicleMileage'}).text
            mileage = re.search(r'\d+', mileage.replace(',', '')).group(0)

            price = item.find('div', {'data-test': 'vehicleCardPricingBlockPrice'}).text.replace(',', '').replace('$', '')

            cursor.execute('INSERT INTO cars values (\''+mileage+'\', \''+price+'\')')
            conn.commit()
            count += 1
            count_in_page += 1
            if count == 20:
                break
    print(count_in_page, car_name, 'were found.')
    page += 1



conn.close()
