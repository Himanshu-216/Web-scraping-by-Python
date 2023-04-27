from bs4 import BeautifulSoup
import requests
import csv
#making a csv file
file = open('csv_file.csv', 'w')
csv_writer = csv.writer(file)
csv_writer.writerow(['Name', 'Price', 'Specifications'])
source = requests.get('https://www.flipkart.com/search?q=google%20pixel%20smartphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off').text
soup = BeautifulSoup(source, 'html5lib')
phone = soup.findAll('div', class_="_4rR01T")
prices = soup.findAll('div',  class_ = "_30jeq3 _1_WHN1")
specs = soup.findAll('ul', class_= "_1xgFaf")

for phones, price, sp in zip(phone, prices, specs):
    ph, pr = phones.text, price.text
    
    print(pr)
    for i in sp:
        print(i.text)
    csv_writer.writerow([str(ph),  str(pr)[1:]+f'.00', [j.text for j in sp]])
    
file.close()




