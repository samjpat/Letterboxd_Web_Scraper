import streamlit as st
import sqlite3


def movie_call(conn, option):
    cur = conn.cursor()
    cur.execute('SELECT name, year, image FROM movie_db WHERE director = ?', (option,))
    rows = cur.fetchmany(8)
    conn.commit()
    return rows




def actor_call(conn, option):
    cur = conn.cursor()
    cur.execute('SELECT actor_id FROM actor_db WHERE name = ?', (option,))
    row = cur.fetchone()
    id = row[0]
    sql = 'SELECT name, year, image FROM movie_db JOIN movie_to_actor ON movie_db.movie_id = movie_to_actor.movie_id WHERE movie_to_actor.actor_id = ?'
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    conn.commit()
    return rows


def genre_call(conn, option):
    cur = conn.cursor()
    cur.execute('SELECT genre_id FROM genre_db WHERE name = ?', (option,))
    row = cur.fetchone()
    id = row[0]
    sql = 'SELECT name, year, image FROM movie_db JOIN movie_to_genre ON movie_db.movie_id = movie_to_genre.movie_id WHERE movie_to_genre.genre_id = ?'
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    conn.commit()
    return rows

def director_call(conn, option):
    cur = conn.cursor()
    cur.execute('SELECT name, year, image FROM movie_db WHERE director = ?', (option,))
    rows = cur.fetchall()
    conn.commit()
    return rows



def main():

    conn = sqlite3.connect("movie_db")
    
    st.title("Movie Recommendations")

    hobby = st.selectbox("Method of reccomendation: ",
                        ['Actor', 'Movie', 'Genre', 'Director'])

    result = []

    if hobby == 'Movie':
        option = st.selectbox("Movie: ", ['Interstellar', 'Parasite'], index = None, placeholder = "Enter a movie...")
        result = movie_call(conn, option)
    elif hobby == 'Actor':
        option = st.selectbox("Actor: ", ['Ryan Gosling', 'Emily Blunt'], index = None, placeholder = "Enter an actor...")
        result = actor_call(conn, option)
    elif hobby == 'Genre':
        option = st.selectbox("Genre: ", ['Horror', 'Action'], index = None, placeholder = "Enter an genre...")
        result = genre_call(conn, option)
    else:
        option = st.selectbox("Director: ", ['Tarantino', 'Williams'], index = None, placeholder = "Enter a director...")
        result = director_call(conn, option)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(result[0][2], width=200)
        st.text(result[0][0], " (", result[0][1], ")")
    with col2:
        st.image(result[1][2], width=200)
        st.text(result[1][0], " (", result[1][1], ")")
    with col3:
        st.image(result[2][2], width=200)
        st.text(result[2][0], " (", result[2][1], ")")

    st.button("New Recommendations")




if __name__ == "__main__":
    main()
