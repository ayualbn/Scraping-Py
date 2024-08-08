from bs4 import BeautifulSoup
import requests
from csv import writer

url ='https://www.truecar.com/used-cars-for-sale/listings/?page=5'

r = requests.get(url) #or site's link in ('')
soup = BeautifulSoup(r.text , 'html.parser')

with open ('usedcarsale.csv' , 'a' , encoding='utf8' , newline='') as f:
    thewriter = writer(f)
    header = ['Title' , 'Miles' , 'Price']
    thewriter.writerow(header)

    for card in soup.select('[class="card-content vehicle-card-body order-3 vehicle-card-carousel-body"]'):
        model = card.select_one('[class="truncate"]').text 
        miles = card.select_one('div[class="flex w-full justify-between"]').text
        price = card.select_one('[class="heading-3 my-1 font-bold"]').text
        
        info = [model , miles , price]
        thewriter.writerow(info)