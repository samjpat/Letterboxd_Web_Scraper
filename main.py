import sqlite3
from scrape import page_get
from scrape import scrape
from scrape import page_scrape

sql_statements = [
    """CREATE TABLE IF NOT EXISTS movie_db (
            movie_id INTEGER PRIMARY KEY,
            name TEXT,
            year INT,
            rating INT,
            director TEXT,
            image TEXT
            
        );""",

    
    """CREATE TABLE IF NOT EXISTS actor_db (
            actor_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
        
        );""",

        
    """CREATE TABLE IF NOT EXISTS movie_to_actor (
            movie_id INTEGER,
            actor_id INTEGER,
            PRIMARY KEY (movie_id, actor_id),
            FOREIGN KEY (movie_id) REFERENCES movie_db(movie_id),
            FOREIGN KEY (actor_id) REFERENCES actor_db(actor_id)
          
        );""",

    """CREATE TABLE IF NOT EXISTS genre_db (
            genre_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE
                
        );""",

    """CREATE TABLE IF NOT EXISTS movie_to_genre (
            movie_id INTEGER,
            genre_id INTEGER,
            PRIMARY KEY (movie_id, genre_id),
            FOREIGN KEY (movie_id) REFERENCES movie_db(movie_id),
            FOREIGN KEY (genre_id) REFERENCES genre_db(genre_id)
        
        );""",

    

]




def main():

    try:
        with sqlite3.connect("movie_db") as conn:
            print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            conn.commit()

    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)


   
    link = "https://letterboxd.com/film/the-whale-2022/"
    scrape(conn, link, 3.66)
    link = "https://letterboxd.com/film/fargo/"
    scrape(conn, link, 4.18)
    link = "https://letterboxd.com/film/the-lobster/"
    scrape(conn, link, 3.75)
    link = "https://letterboxd.com/film/a-complete-unknown/"
    scrape(conn, link, 3.55)
    link = "https://letterboxd.com/film/trainspotting/"
    scrape(conn, link, 4.22)
    link = "https://letterboxd.com/film/legally-blonde/"
    scrape(conn, link, 3.82)
    link = "https://letterboxd.com/film/corpse-bride/"
    scrape(conn, link, 3.89)
    link = "https://letterboxd.com/film/deadpool-2/"
    scrape(conn, link, 3.48)
    link = "https://letterboxd.com/film/in-the-mood-for-love/"
    scrape(conn, link, 4.39)
    link = "https://letterboxd.com/film/the-pianist/"
    scrape(conn, link, 4.40)
    link = "https://letterboxd.com/film/the-martian/"
    scrape(conn, link, 3.78)
    link = "https://letterboxd.com/film/the-iron-claw-2023/"
    scrape(conn, link, 4.11)
    link = "https://letterboxd.com/film/alien-romulus/"
    scrape(conn, link, 3.59)
    link = "https://letterboxd.com/film/13-going-on-30-3/"
    scrape(conn, link, 3.63)


    link = "https://letterboxd.com/film/dont-worry-darling/"
    scrape(conn, link, 3.05)
    link = "https://letterboxd.com/film/leon-the-professional/"
    scrape(conn, link, 4.01)
    link = "https://letterboxd.com/film/bodies-bodies-bodies/"
    scrape(conn, link, 3.28)
    link = "https://letterboxd.com/film/the-florida-project/"
    scrape(conn, link, 4.10)
    link = "https://letterboxd.com/film/notting-hill/"
    scrape(conn, link, 3.66)
    link = "https://letterboxd.com/film/the-hangover/"
    scrape(conn, link, 3.69)
    link = "https://letterboxd.com/film/captain-america-the-first-avenger/"
    scrape(conn, link, 3.32)
    link = "https://letterboxd.com/film/heretic-2024/"
    scrape(conn, link, 3.33)
    link = "https://letterboxd.com/film/the-conjuring/"
    scrape(conn, link, 3.60)
    link = "https://letterboxd.com/film/saving-private-ryan/"
    scrape(conn, link, 4.25)
    link = "https://letterboxd.com/film/rogue-one-a-star-wars-story/"
    scrape(conn, link, 3.79)
    link = "https://letterboxd.com/film/your-name/"
    scrape(conn, link, 4.22)


    link = "https://letterboxd.com/film/28-days-later/"
    scrape(conn, link, 3.73)
    link = "https://letterboxd.com/film/no-hard-feelings-2023/"
    scrape(conn, link, 2.99)
    link = "https://letterboxd.com/film/kpop-demon-hunters/"
    scrape(conn, link, 3.63)
    link = "https://letterboxd.com/film/star-wars-episode-ii-attack-of-the-clones/"
    scrape(conn, link, 3.01)
    link = "https://letterboxd.com/film/the-big-lebowski/"
    scrape(conn, link, 4.12)
    link = "https://letterboxd.com/film/cars/"
    scrape(conn, link, 3.83)
    link = "https://letterboxd.com/film/ferris-buellers-day-off/"
    scrape(conn, link, 3.95)
    link = "https://letterboxd.com/film/city-of-god/"
    scrape(conn, link, 4.55)
    link = "https://letterboxd.com/film/the-zone-of-interest/"
    scrape(conn, link, 3.86)
    link = "https://letterboxd.com/film/the-french-dispatch/"
    scrape(conn, link, 3.67)
    link = "https://letterboxd.com/film/grave-of-the-fireflies/"
    scrape(conn, link, 4.47)
    link = "https://letterboxd.com/film/civil-war-2024/"
    scrape(conn, link, 3.55)




    #statement = '''DELETE FROM movie_db'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DELETE FROM actor_db'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DELETE FROM genre_db'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DELETE FROM movie_to_actor'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DELETE FROM movie_to_genre'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()

    #statement = '''DROP TABLE movie_db'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DROP TABLE actor_db'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DROP TABLE genre_db'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DROP TABLE movie_to_actor'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()
    #statement = '''DROP TABLE movie_to_genre'''
    #cur = conn.cursor()
    #cur.execute(statement)
    #conn.commit()

    #page_format = "https://letterboxd.com/films/popular/page/4/"

    
    #link = page_format

    #for i in range(1):
    #    if(i > 1):
    #    link = link + "page/" + i + "/"
    #    movie_titles = page_get(link)
    #    page_scrape(movie_titles)

    #movie_titles = page_get(link)
    #page_scrape(conn, movie_titles)
    
    conn.close()


if __name__ == "__main__":
    main()
