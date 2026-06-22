import pickle
import pandas as pd
import streamlit as st
import os
import gdown

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

# Download similarity.pkl from Google Drive if not present
if not os.path.exists("similarity.pkl"):
    file_id = "1ySCmERuViKh8HG-h06abptN-6bMG-Ofe"

    url = f"https://drive.google.com/uc?id={file_id}"

    gdown.download(
        url,
        "similarity.pkl",
        quiet=False
    )

similarity = pickle.load(open("similarity.pkl", "rb"))

# ---------------- RECOMMEND FUNCTION ---------------- #
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 0;
}

.subtitle {
    text-align: center;
    color: #9ca3af;
    font-size: 1.1rem;
    margin-bottom: 2rem;
}

.movie-card {
    background-color: #1f2937;
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-bottom: 15px;
    border: 1px solid #374151;
}

.movie-title {
    color: white;
    font-size: 18px;
    font-weight: 600;
}

.rank {
    font-size: 24px;
    color: #60a5fa;
    font-weight: bold;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown(
    '<p class="main-title">🎬 Movie Recommender System</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Find movies similar to your favorites using Machine Learning</p>',
    unsafe_allow_html=True
)

# ---------------- MOVIE SELECT ---------------- #
selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movies['title'].values
)

# ---------------- BUTTON ---------------- #
if st.button("🎬 Get Recommendations", use_container_width=True):

    recommendations = recommend(selected_movie)

    st.markdown(
        f"## 🎯 Because you liked *{selected_movie}*"
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for idx, movie in enumerate(recommendations):
        with cols[idx]:
            st.markdown(
                f"""
                <div class="movie-card">
                    <div class="rank">⭐ #{idx+1}</div>
                    <div class="movie-title">{movie}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("---")

st.caption(
    "Built with Python • Pandas • Scikit-Learn • Cosine Similarity • Streamlit"
)