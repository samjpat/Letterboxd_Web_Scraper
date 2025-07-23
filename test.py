import requests
from bs4 import BeautifulSoup
import json
import sqlite3


link = 'https://letterboxd.com/film/everything-everywhere-all-at-once/'

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

count = 0
cast_soup = soup.find('div', {'class': 'cast-list text-sluglist'})
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



print(name)
print(year)
print(director)
for temp in cast:
    print(temp)
for temp in genres:
    print(temp)
print(image)

#sql_statements = [
#    """CREATE TABLE IF NOT EXISTS movie (
#            movie_id INT PRIMARY KEY AUTO_INCREMENT,
#            name TEXT,
#            year INT,
#            rating INT,
#            director TEXT,
#            image TEXT
#            
#        );""",

#    """CREATE TABLE IF NOT EXISTS movie_to_actor (
#            movie_id INT PRIMARY KEY,
#           actor_id INT
                
#        );""",

#    """CREATE TABLE IF NOT EXISTS actor (
#            actor_id INT PRIMARY KEY AUTO_INCREMENT,
#            name TEXT 
#        
#        );"""

#]

#def add_movie(conn, movie):
#    sql = ''' INSERT INTO movie(movie_id, name, year, rating, director, image)
#              VALUES(?,?,?,?,?,?)'''
#    
#    cur = conn.cursor()

#    cur.execute(sql, movie)

#    conn.commit()

#    return cur.lastrowid

#try:
#    with sqlite3.connect("movie_db") as conn:
#        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

        #cursor = conn.cursor()
        #for statement in sql_statements:
        #    cursor.execute(statement)
        #conn.commit()

#        movie = ('1', 'Interstellar', '2014', '4.0' ,'Nolan', 'image_test')
#        movie_id = add_movie(conn, movie)
#        print(f'Created a movie with the id {movie_id}')


#except sqlite3.OperationalError as e:
#    print("Failed to open database:", e)
