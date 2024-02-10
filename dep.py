import pandas as pd
import streamlit as st
import pickle
import requests
import sys
import os
import shutil


def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}'
        '?api_key=ec437c9d440e19caff79e1b380110413&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movies, sim, movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sim[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommendations.append(movies.iloc[i[0]].title)
        movie_posters.append(fetch_poster(movie_id))
    return recommendations, movie_posters


def main():
    data_directory = 'data'
    shutil.unpack_archive(f'{data_directory}.zip', data_directory)

    movies_dict = pickle.load(
        open(os.path.join(data_directory, 'movie_dict.pkl'), 'rb'))
    movies = pd.DataFrame(movies_dict)

    sim = pickle.load(
        open(os.path.join(data_directory, 'sim.pkl'), 'rb'))

    st.title('Movie Recommender')
    selectedTitle = st.selectbox('How would you like to be contacted?',
                                 movies['title'].values)

    if not st.button('Recommend'):
        return

    names, posters = recommend(movies, sim, selectedTitle)

    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            st.image(posters[i])


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
