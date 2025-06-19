import requests
from bs4 import BeautifulSoup
import json

from selen import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


#url = 'https://letterboxd.com/film/parasite-2019/'

#response = requests.get(url)

#soup = BeautifulSoup(response.content, 'html.parser')

#details = soup.find(class_ = "details")

#print(details.text)


#genres = soup.find('div', {'class': 'text-sluglist capitalize'})
#for genre in genres.find_all('a', {'class': 'text-slug'}):
#    print(genre.text)

#print("\n")

#casts = soup.find('div', {'class': 'cast-list text-sluglist'})
#for cast in casts.find_all('a', {'class': 'text-slug tooltip'}):
#    print(cast.text)

#soup_image = BeautifulSoup(response.text, 'html.parser')

#script_w_data = soup_image.select_one('script[type="application/ld+json"]')
#json_obj = json.loads(script_w_data.text.split(' */')[1].split('/* ]]>')[0])


#print(json_obj['image'])


#resp = requests.get(link)

#soup = BeautifulSoup(resp.content, 'lxml')

#info = soup.find('body')
#info2 = info.find(id = 'content')
#info3 = info2.find(class_ = 'content-wrap')
#info4 = info3.find(class_ = 'section col-24 col-main')
#info5 = info4.find_all(id = 'films-browser-list-container')
#print(info5)





link = 'https://letterboxd.com/films/popular/'
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get(link)

info = driver.find_elements(By.ID, "content")
print(info)


driver.quit()
