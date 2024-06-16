# Importing the Required Libraries
import streamlit as st
import pickle
import requests

# Loading the necessary Files
movies = pickle.load(open('movies.pkl', 'rb'))
movie_list = movies.title
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Creating the function to get the poster path of a movie given a movie id
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MjcwZGY1ZjUyYzFiZDU3ZTY5YzE3ZjgwNWI1OTllYiIsInN1YiI6IjY2MTUwN2M4YTZhNGMxMDE4NmJlYzA0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.CSxoWYoWnqPEDjctHsr0PRwMV9lOgiOsi-h14jpw4I8"
        }
    response = requests.get(url, headers=headers)
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data ['poster_path']



# Creating a function for fetching Recommended Movie Names and their Poster Path using the fetch_poster function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Title of the Application
st.title('Movie Recommender System')

# Putting the Select Box to choose Movies
selected_movie = st.selectbox('Select Your Movie', movie_list)

# Creating the Button and its functionality using the recommend function
if st.button('Recommend Me Movies like the above: '):
    names, posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])