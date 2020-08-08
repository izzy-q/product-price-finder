#importing
from bs4 import BeautifulSoup as soup
import requests
import csv


#user-agent string and website url
url = "https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_1"
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
}


#gets webpage
website = requests.get(url, headers=header).text
content = soup(website, 'lxml')


#list of all product titles and prices
titles = []
prices = []


#finds the titles of all products and appends them to (list:titles)
for title in content.find_all(class_="a-size-medium a-color-base a-text-normal"):
    titles.append(title.text)


#finds the prices of all products and appends them to (list:prices)
for price in content.find_all(class_="a-price"):
    prices.append(price.text.split('$')[-1])


with open("moniters.csv", 'w') as file: 
    writer = csv.writer(file)
    writer.writerow(["PRODUCT TITLE", "PRICE", "RATING"])

    #adds product title and price for each product to a csv file
    for i in range(len(titles)):
        writer.writerow([titles[i], prices[i]])


