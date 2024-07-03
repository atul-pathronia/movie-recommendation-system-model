import streamlit as st
import pickle
import requests


movies = pickle.load(open("movies.pkl","rb"))
similarity_matrix = pickle.load(open("similarity_matrix.pkl","rb"))

def recommend_func(movie):
    try:
        movie_index = movies[movies["title"] == movie].index[0]
        distance = similarity_matrix[movie_index]
        movies_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

        url = "https://image.tmdb.org/t/p/w500/"

        recommended_movies = []
        recommended_poster = []
        for i in movies_list:
            print(movies.iloc[i[0]])
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_poster.append(url+movies.iloc[i[0]].backdrop_path)
        return recommended_movies,recommended_poster
    except ValueError:
        print(ValueError)


# def movie_poster(movie_id):
#     print(movie_id)
#     url = "https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNzAxMmFhYmFjOGM4OTM2NWQxODJjMWEwYzdmNWFlZiIsInN1YiI6IjY2NmIwYWQ5YjEyM2I5NzFkNzM4MjUzMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.G7gJFSRmMVupBE8XTNXXFPsBumwOGdNJBotNO4daYQ4"
#     }

#     response = requests.get(url, headers=headers)
#     print(response.text)


st.title("Movies Recommendation System")

selected_movie_name = st.selectbox("Select your movie",movies["title"].values)

if st.button("Recommend"):
    name,poster = recommend_func(selected_movie_name)
    col1, col2 = st.columns([.5,.5])
    with col1:
        st.text(name[0])
        st.image(poster[0])

    with col2:
        st.text(name[1])
        st.image(poster[1])
    
    col3, col4 = st.columns([.5,.5])
    with col3:
        st.text(name[2])
        st.image(poster[2])

    with col4:
        st.text(name[3])
        st.image(poster[3])
