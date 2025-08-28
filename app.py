import streamlit as st
import pickle
import pandas as pd
import requests
from io import BytesIO

# ----------------------------
# URLs for your pickle files
# Replace these with your actual GitHub raw URLs
MOVIES_URL = "https://raw.githubusercontent.com/YourUserName/your-pkl-repo/main/movies_dict.pkl"
SIMILARS_URL = "https://raw.githubusercontent.com/YourUserName/your-pkl-repo/main/similars.pkl"


# ----------------------------

@st.cache_data
def load_pickle_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return pickle.load(BytesIO(response.content))


# Load data
movie_dict = load_pickle_from_url(MOVIES_URL)
similars = load_pickle_from_url(SIMILARS_URL)

movies = pd.DataFrame(movie_dict)

# ---- Custom CSS ----
st.markdown("""
<style>
/* App background gradient */
.stApp {
    background: linear-gradient(
        270deg,
        rgba(255,0,0,0.3),
        rgba(255,165,0,0.3),
        rgba(255,192,203,0.3),
        rgba(255,0,0,0.3)
    );
    background-size: 400% 400%;
    animation: gradientBG 6s linear infinite;
    color: #ecf0f1;
}

/* Gradient animation keyframes */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Main title with red glow */
.main-title {
    font-size: 52px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    background: linear-gradient(
        270deg,
        rgba(255,75,43,1),
        rgba(255,0,0,1)
    );
    background-size: 800% 800%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 4px rgba(255,75,43,0.6),
                 0 0 8px rgba(255,0,0,0.6);
    animation: luminousFlow 6s linear infinite;
}

@keyframes luminousFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Movie cards container */
.movie-card-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 20px;
}

/* Movie cards */
.movie-card {
    display: inline-block;
    background: #2c3e50; 
    border-radius: 18px;
    padding: 20px;
    margin: 12px;
    text-align: center;
    width: 200px;
    position: relative;
    color: #ecf0f1;
    font-weight: 600;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    overflow: hidden;
}

/* Hover: pink/orange gradient glow */
.movie-card:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 12px 25px rgba(255,100,100,0.6);
    background: linear-gradient(270deg, #ff4b2b, #ff9068, #ff2b6b, #ff7a59, #ff4b2b);
    background-size: 600% 600%;
    animation: hoverGradientFlow 4s ease infinite;
}

@keyframes hoverGradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.movie-title {
    margin-top: 15px;
    font-size: 18px;
    text-shadow: 0 0 3px rgba(0,0,0,0.5);
}

/* Responsive adjustments */
@media (max-width: 600px) {
    .movie-card {
        width: 90%;
        margin: 10px auto;
        padding: 15px;
    }
    .main-title { font-size: 42px; }
}
</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<div class='main-title'>🍿 Movie Recommendation System</div>", unsafe_allow_html=True)

# ---- Search box ----
selected_movie_name = st.selectbox(
    '<h2 style="text-align:center;">Search your favorite movie 🎥</h2>',
    movies.title.values,
    key='movie_select'
)


# ---- Recommendation logic ----
def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similars[movie_idx]
    e_distances = list(enumerate(distances))
    similar = sorted(e_distances, reverse=True, key=lambda x: x[1])[1:11]
    return [movies.iloc[i[0]].title for i in similar]


# ---- Recommend button ----
if st.button('✨ Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown("<h3 style='text-align:center;'>🔥 Top Recommendations for You:</h3>", unsafe_allow_html=True)

    # Render movie cards
    movie_cards = "<div class='movie-card-container'>"
    for rec in recommendations:
        movie_cards += f"<div class='movie-card'>🎬<div class='movie-title'>{rec}</div></div>"
    movie_cards += "</div>"
    st.markdown(movie_cards, unsafe_allow_html=True)
