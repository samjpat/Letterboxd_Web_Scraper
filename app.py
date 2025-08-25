import streamlit as st
import sqlite3
import itertools


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
    sql = 'SELECT name, year, image FROM movie_db JOIN movie_to_actor ON movie_db.movie_id = movie_to_actor.movie_id WHERE movie_to_actor.actor_id = ? ORDER BY rating DESC'
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    conn.commit()
    return rows


def genre_call(conn, option):
    cur = conn.cursor()
    cur.execute('SELECT genre_id FROM genre_db WHERE name = ?', (option,))
    row = cur.fetchone()
    id = row[0]
    sql = 'SELECT name, year, image FROM movie_db JOIN movie_to_genre ON movie_db.movie_id = movie_to_genre.movie_id WHERE movie_to_genre.genre_id = ? ORDER BY rating DESC'
    cur.execute(sql, (id,))
    rows = cur.fetchall()
    conn.commit()
    return rows

def director_call(conn, option):
    cur = conn.cursor()
    cur.execute('SELECT name, year, image FROM movie_db WHERE director = ? ORDER BY rating DESC', (option,))
    rows = cur.fetchall()
    conn.commit()
    return rows


def main():

    conn = sqlite3.connect("movie_db")
    

    sql = '''SELECT name FROM movie_db'''
    cur = conn.cursor()
    cur.execute(sql)
    movies = list(itertools.chain(*cur.fetchall()))

    sql = '''SELECT name FROM actor_db'''
    cur = conn.cursor()
    cur.execute(sql)
    actors = list(itertools.chain(*cur.fetchall()))

    sql = '''SELECT name FROM genre_db'''
    cur = conn.cursor()
    cur.execute(sql)
    genres = list(itertools.chain(*cur.fetchall()))

    sql = '''SELECT director FROM movie_db'''
    cur = conn.cursor()
    cur.execute(sql)
    directors = list(itertools.chain(*cur.fetchall()))


    st.title("Movie Recommendations")
    type = st.selectbox("Method of reccomendation: ",
                        ['Actor', 'Movie', 'Genre', 'Director'])
    
    

    if type == 'Movie':
        option = st.selectbox("Movie: ", movies, index = None, placeholder = "Enter a movie...")
    elif type == 'Actor':
        option = st.selectbox("Actor: ", actors, index = None, placeholder = "Enter an actor...")
    elif type == 'Genre':
        option = st.selectbox("Genre: ", genres, index = None, placeholder = "Enter an genre...")
    else:
        option = st.selectbox("Director: ", directors, index = None, placeholder = "Enter a director...")
         
    enter = st.button("Enter")
    col1, col2, col3 = st.columns(3)


    if enter:
        if "result" not in st.session_state:
            st.session_state.result = []
        
        if "movie_num" not in st.session_state:
            st.session_state.movie_num = 0

        if type == 'Movie':
            st.session_state.result = movie_call(conn, option)
        elif type == 'Actor':
            st.session_state.result = actor_call(conn, option)
        elif type == 'Genre':
            st.session_state.result = genre_call(conn, option)
        else:
            st.session_state.result = director_call(conn, option)

        with col1:
            if len(st.session_state.result) > 0:
                st.image(st.session_state.result[0][2], width=200)
                st.text(f"{st.session_state.result[0][0]}  ({st.session_state.result[0][1]})")
        with col2:
            if len(st.session_state.result) > 1:
                st.image(st.session_state.result[1][2], width=200)
                st.text(f"{st.session_state.result[1][0]}  ({st.session_state.result[1][1]})")
        with col3:
            if len(st.session_state.result) > 2:
                st.image(st.session_state.result[2][2], width=200)
                st.text(f"{st.session_state.result[2][0]}  ({st.session_state.result[2][1]})")


    if st.button("New Recommendations"):
        #if type == 'Movie':
        #    result = movie_call(conn, option)
        #elif type == 'Actor':
        #    result = actor_call(conn, option)
        #elif type == 'Genre':
        #    result = genre_call(conn, option)
        #else:
        #    result = director_call(conn, option)
        
        
        st.session_state.movie_num =  st.session_state.movie_num + 3
        
        with col1:
            if len(st.session_state.result) > st.session_state.movie_num:
                st.image(st.session_state.result[st.session_state.movie_num][2], width=200)
                st.text(f"{st.session_state.result[st.session_state.movie_num][0]}  ({st.session_state.result[st.session_state.movie_num][1]})")
        with col2:
            if len(st.session_state.result) > st.session_state.movie_num+1:
                st.image(st.session_state.result[st.session_state.movie_num+1][2], width=200)
                st.text(f"{st.session_state.result[st.session_state.movie_num+1][0]}  ({st.session_state.result[st.session_state.movie_num+1][1]})")
        with col3:
            if len(st.session_state.result) > st.session_state.movie_num+2:
                st.image(st.session_state.result[st.session_state.movie_num+2][2], width=200)
                st.text(f"{st.session_state.result[st.session_state.movie_num+2][0]}  ({st.session_state.result[st.session_state.movie_num+2][1]})")



if __name__ == "__main__":
    main()
