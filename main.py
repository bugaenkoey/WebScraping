import requests
from bs4 import BeautifulSoup

url = "https://sport.ua/uk/rss/all/"
page = requests.get(url)
soup = BeautifulSoup(page.content, "xml")
#print(soup)
items = soup.find_all('item')
item = items[0]

def get_info(item):
  title = item.find('title').text
  link = item.find('link').text
  picture = item.find('enclosure').get("url")
  description = item.find('description').text
  category_item = item.find_all("category")
  category = []
  for el in category_item:
    category.append(el.text)
  date = item.find('pubDate').text
  info = {"title":title,"link":link,"picture":picture,"description":description,"category":category,"date":date}
  return info

news = []

for item in items:
  info = get_info(item)
  news.append(info)

print(news)

import csv
with open("news_sport_ua.csv","w",newline="") as file:
  fieldnames = ["title","link","picture","description","category","date"]
  writer = csv.DictWriter(file,fieldnames=fieldnames,delimiter=",")
  writer.writeheader()
  writer.writerows(news)