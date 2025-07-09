from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import requests
import json
import sqlite3



def page_get(link):
    driver = Firefox()
    movie_titles = []
    driver.get(link)
    sleep(0.5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    info = soup.find_all('li', class_ = 'listitem poster-container')
    for item in info:
        movie_titles.append(item.find('div')['data-film-slug'])
    driver.quit()
    return movie_titles

def scrape(link):
    print("Scraping", link)
    name = ""
    director = ""
    cast = []
    genres = []
    image = ''
    

    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    name = soup.find(class_ = 'name js-widont prettify').text
    year = soup.find(class_ = 'releasedate').text
    director = soup.find(class_ = 'creatorlist').text

    cast_soup = soup.find('div', {'class': 'cast-list text-sluglist'})
    count = 0
    for temp in cast_soup.find_all('a', {'class': 'text-slug tooltip'}):
        cast.append(temp.text)
        if count > 15:
            break
        count = count + 1

    genre_soup = soup.find('div', {'class': 'text-sluglist capitalize'})
    for temp in genre_soup.find_all('a', {'class': 'text-slug'}):
        genres.append(temp.text)

    script_w_data = soup.select_one('script[type="application/ld+json"]')
    json_obj = json.loads(script_w_data.text.split(' */')[1].split('/* ]]>')[0])
    image = json_obj['image']

    rating = soup.find(class_ = "tooltip display-rating").text

    print("Scraped ", name)
        
    #sql = ''' INSERT INTO movie_db(name, year, rating, director, image)
    #                VALUES(?,?,?,?,?,?)'''
    #movie = (name, year, rating, director, image)
    #cur = conn.cursor()
    #cur.execute(sql, movie)
    #conn.commit()

    #cur = conn.execute("SELECT movie_id from movie_db WHERE name = ?", (name,))
    #conn.commit()
    #movie_id = cur[0]
    
    #for genre in genres:
    #    sql = '''INSERT INTO genre_db(name) VALUES(?)'''
    #    cur = conn.cursor()
    #    cur.execute(sql, genre)
    #    conn.commint()
        


    #for actor in cast:
    #    sql = '''INSERT INTO actor_db(name) VALUES(?)'''
    #    cur = conn.cursor()
    #    cur.execute(sql, actor)
    #    conn.commint()

    

    
    



def page_scrape(movie_titles):
    link_format = "https://letterboxd.com/film/"
    for title in movie_titles:
        link = link_format + title + '/'
        scrape(link)


