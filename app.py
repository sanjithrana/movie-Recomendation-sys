import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open("movie_dict.pkl","rb"))
movies =  pd.DataFrame(movies_dict)  # movies_list['title'].values
similarity = pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
  # Fix: Using the movie variable instead of the string 'movie'
  movie_index = movies[movies['title'] == movie].index[0]
  distance = similarity[movie_index]
  movies_list = sorted(list(enumerate(distance)),reverse=True,key = lambda x: x[1])[1:6]
  
  recommended_movies = []
  for i in movies_list:
    recommended_movies.append(movies['title'][i[0]] ) # printing movie title instead of index
  return recommended_movies

st.title("movie recommened sys")

selecteion_of_movies = st.selectbox(
'Enter a Movie Name',
movies['title'].values)


if st.button("Recommed"):
    recommendation = recommend(selecteion_of_movies)
    for i in recommendation:
        st.write(i)
