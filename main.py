import sqlite3
from scrape import page_get
from scrape import scrape
from scrape import page_scrape

sql_statements = [
    """CREATE TABLE IF NOT EXISTS movie_db (
            movie_id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT,
            year INT,
            rating INT,
            director TEXT,
            image TEXT
            
        );""",

    
    """CREATE TABLE IF NOT EXISTS actor_db (
            actor_id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT UNIQUE
        
        );""",

        
    """CREATE TABLE IF NOT EXISTS movie_to_actor (
            movie_id INT PRIMARY KEY,
            actor_id INT PRIMARY KEY,
            FOREIGN KEY (movie_id) REFERENCES movie_db(movie_id),
            FOREIGN KEY (actor_id) REFERENCES actor_db(actor_id)
          
        );""",

    """CREATE TABLE IF NOT EXISTS genre_db (
            genre_id INT AUTO_INCREMENT PRIMARY KEY,
            name TEXT UNIQUE
                
        );""",

    """CREATE TABLE IF NOT EXISTS movie_to_genre (
            movie_id INT PRIMARY KEY,
            genre_id INT PRIMARY KEY,
            FOREIGN KEY (movie_id) REFERENCES movie_db(movie_id),
            FOREIGN KEY (genre_id) REFERENCES genre_db(genre_id)
        
        );""",

    

]




def main():

    #try:
    #    with sqlite3.connect("movie_db") as conn:
    #        print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")

    #        cursor = conn.cursor()
    #        for statement in sql_statements:
    #            cursor.execute(statement)
    #        conn.commit()

    #except sqlite3.OperationalError as e:
    #    print("Failed to open database:", e)





    page_format = "https://letterboxd.com/films/popular/"

    
    link = page_format

    #for i in range(1):
    #    if(i > 1):
    #        link = link + "page/" + i + "/"
    #    movie_titles = page_get(link)
    #    page_scrape(movie_titles)

    movies = page_get(link)
    page_scrape(movies)


if __name__ == "__main__":
    main()
