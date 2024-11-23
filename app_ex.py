import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open("movie_dict.pkl","rb"))
movies =  pd.DataFrame(movies_dict)  # movies_list['title'].values
similarity = pickle.load(open("similarity.pkl","rb"))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
  # Fix: Using the movie variable instead of the string 'movie'
  movie_index = movies[movies['title'] == movie].index[0]
  distance = similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x: x[1])[1:6]
  
  recommended_movies = []
  recommended_movies_poster = []
  for i in movies_list:
    movie_id = movies['movie_id'][i[0]]
    recommended_movies.append(movies['title'][i[0]] ) # printing movie title instead of index
    recommended_movies_poster.append(fetch_poster(movie_id))
  return recommended_movies,recommended_movies_poster

st.title("movie recommened sys")

selecteion_of_movies = st.selectbox(
'Enter a Movie Name',
movies['title'].values)


if st.button("Recommed"):
    names,poste = recommend(selecteion_of_movies)
   
    col1, col2, col3 , col4,col5= st.columns(5)
    with col1:
       st.text(names[0])
       st.image(poste[0])
    with col2:
       st.text(names[1])
       st.image(poste[1])
    with col3:
       st.text(names[2])
       st.image(poste[2])
    with col4:
       st.text(names[3])
       st.image(poste[3])
    with col5:
       st.text(names[4])
       st.image(poste[4])

