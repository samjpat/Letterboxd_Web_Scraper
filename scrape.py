from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
import requests
import json
import sqlite3
import random



def page_get(link):
    driver = Firefox()
    movie_titles = []
    driver.get(link)
    sleep(0.5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    info = soup.find_all('li', class_ = 'listitem poster-container')
    for item in info:
        movie_titles.append((item.find('div')['data-film-slug'], item.find('a')['data-original-title'][-4:]))
    driver.quit()
    return movie_titles

def scrape(conn, link, rating):
    name = ""
    director = ""
    cast = []
    genres = []
    image = ''
    
    sleep(random.uniform(0, 5))
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')

    name = soup.find(class_ = 'name js-widont prettify').text
    sleep(random.uniform(0, 5))
    year = soup.find(class_ = 'releasedate').text
    director = soup.find(class_ = 'creatorlist').text

    cast_soup = soup.find('div', {'class': 'cast-list text-sluglist'})
    count = 0
    for temp in cast_soup.find_all('a', {'class': 'text-slug tooltip'}):
        sleep(random.uniform(0, .8))
        cast.append(temp.text)
        if count > 13:
            break
        count = count + 1

    sleep(random.uniform(0, 5))


    genre_soup = soup.find('div', {'class': 'text-sluglist capitalize'})
    for temp in genre_soup.find_all('a', {'class': 'text-slug'}):
        sleep(random.uniform(0, .8))
        genres.append(temp.text)

    script_w_data = soup.select_one('script[type="application/ld+json"]')
    json_obj = json.loads(script_w_data.text.split(' */')[1].split('/* ]]>')[0])
    image = json_obj['image']

    sleep(random.uniform(0, 5))
        
    sql = ''' INSERT INTO movie_db(name, year, rating, director, image)
              VALUES(?,?,?,?,?) '''
    movie = (name, year, rating, director, image)
    cur = conn.cursor()
    cur.execute(sql, movie)
    conn.commit()

    #cur = conn.execute("SELECT movie_id from movie_db WHERE name = ?", (name,))
    #conn.commit()
    #movie_id = cur[0]

    sql = '''SELECT COUNT(*) FROM movie_db'''
    cur = conn.cursor()
    cur.execute(sql)
    movie_id = cur.fetchone()[0]

    
    for genre in genres:
        sql = '''INSERT OR IGNORE INTO genre_db(name) VALUES(?)'''
        cur = conn.cursor()
        cur.execute(sql, [genre])
        conn.commit()

        sql = '''SELECT genre_id FROM genre_db WHERE name = ?'''
        cur = conn.cursor()
        cur.execute(sql, (genre,))
        genre_id = cur.fetchone()[0]

        sql = '''INSERT INTO movie_to_genre (movie_id, genre_id) VALUES(?, ?)'''
        info = (movie_id, genre_id)
        cur = conn.cursor()
        cur.execute(sql, info)
        conn.commit()



    for actor in cast:
        sql = '''INSERT OR IGNORE INTO actor_db(name) VALUES(?)'''
        cur = conn.cursor()
        cur.execute(sql, [actor])
        conn.commit()

        sql = '''SELECT actor_id FROM actor_db WHERE name = ?'''
        cur = conn.cursor()
        cur.execute(sql, (actor,))
        actor_id = cur.fetchone()[0]

        sql = '''INSERT INTO movie_to_actor (movie_id, actor_id) VALUES(?, ?)'''
        info = (movie_id, actor_id)
        cur = conn.cursor()
        cur.execute(sql, info)
        conn.commit()

        

    

    
def page_scrape(movie_titles):
    link_format = "https://letterboxd.com/film/"
    for title in movie_titles:
        link = link_format + title[0] + '/'
        scrape(link, title[1])


