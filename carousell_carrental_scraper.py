from bs4 import BeautifulSoup as bs
import requests
import csv
from csv import writer
import datetime
import schedule
import time

url = "https://www.carousell.sg/categories/cars-32/car-rental-singapore-1181/?sc=1202081422120a0c74696d655f63726561746564120208002a150a0b636f6c6c656374696f6e7322060a04313138313a0408bbe17242037765624a02656e&sort_by=time_created%2Cdescending"

source = requests.get(url).text
soup = bs(source,features="html.parser")

main = soup.find('main').div.div.div

items = main.findChildren('div',recursive=False)

for item in items:
    try:
        item = item.div
        
        name = item.a.find_all('div')[1].p.text
    
        time = item.a.find_all('div')[1].div.p.text

        car = item.find_all('a')[1].p.text

        price = item.find_all('a')[1].find_all('p')[2].text

        bumped = item.a.find_all('div')[1].div.svg

        if bumped:
            bump = "yes"
        else:
            bump = "no"
        
        print(name)
        print(car)
        print(time)
        print(price)
        print(bump)
    except:
        continue

