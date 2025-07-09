import streamlit as st


st.title("Movie Recommendations")

hobby = st.selectbox("Method of reccomendation: ",
                     ['Actor', 'Movie', 'Genre', 'Director'])

if hobby == 'Movie':
    st.selectbox("Movie: ", ['Interstellar', 'Parasite'], index = None, placeholder = "Enter a movie...")
elif hobby == 'Actor':
    st.selectbox("Actor: ", ['Ryan Gosling', 'Emily Blunt'], index = None, placeholder = "Enter an actor...")
elif hobby == 'Genre':
    st.selectbox("Genre: ", ['Horror', 'Action'], index = None, placeholder = "Enter an genre...")
else:
    st.selectbox("Director: ", ['Tarantino', 'Williams'], index = None, placeholder = "Enter a director...")

col1, col2, col3 = st.columns(3)

#st.image("https://a.ltrbxd.com/resized/film-poster/1/1/7/6/2/1/117621-interstellar-0-230-0-345-crop.jpg?v=7ad89e6666", width=200)
#st.image("https://a.ltrbxd.com/resized/film-poster/4/2/6/4/0/6/426406-parasite-0-230-0-345-crop.jpg?v=8f5653f710", width=200)

with col1:
    st.image("https://a.ltrbxd.com/resized/film-poster/1/1/7/6/2/1/117621-interstellar-0-230-0-345-crop.jpg?v=7ad89e6666", width=200)
    st.text("Interstellar (2014)")
with col2:
    st.image("https://a.ltrbxd.com/resized/film-poster/4/2/6/4/0/6/426406-parasite-0-230-0-345-crop.jpg?v=8f5653f710", width=200)
    st.text("Parasite (2019)")
with col3:
    st.image("https://a.ltrbxd.com/resized/film-poster/2/5/1/9/4/3/251943-spider-man-into-the-spider-verse-0-1000-0-1500-crop.jpg?v=538fe0ada6", width=200)
    st.text("Spider-Man: Into the Spider-Verse (2019)")

st.button("New Recommendations")
