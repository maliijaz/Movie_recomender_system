import streamlit as st
import pickle
import pandas as pd
import movieposters as mp

similarity = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
      movie_index = movies[movies['title'] == movie].index[0]
      distances = similarity[movie_index]
      movies_sorted = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
      
      recommended_movies = []
      recommended_movies_posters = []
      for i in movies_sorted:
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(mp.get_poster(movies.iloc[i[0]].title))
      
      return recommended_movies,recommended_movies_posters

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
movies_list = movies['title'].values

st.title("Movie Recommender System")

selected_movie = st.selectbox(
      'Select a movie',
      movies_list)


if st.button('Recommend'):
      recommended_movies, recommended_movies_posters = recommend(selected_movie)
      col1, col2, col3, col4, col5 = st.columns(5)

      with col1:
            st.write(recommended_movies[0])
            st.image(recommended_movies_posters[0])

      with col2:
            st.write(recommended_movies[1])
            st.image(recommended_movies_posters[1])

      with col3:
            st.write(recommended_movies[2])
            st.image(recommended_movies_posters[2])

      with col4:
            st.write(recommended_movies[3])
            st.image(recommended_movies_posters[3])

      with col5:
            st.write(recommended_movies[4])
            st.image(recommended_movies_posters[4])

