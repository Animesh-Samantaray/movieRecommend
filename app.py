import streamlit as st
import pickle
import pandas as pd

# Load movie data
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similars = pickle.load(open('similars.pkl', 'rb'))

movies = pd.DataFrame(movie_dict)

# ---- Custom CSS ----
st.markdown("""
    <style>
    /* Dark background with gradient animation */
.stApp {
    background: linear-gradient(
        270deg,
        rgba(255,0,0,0.3),
        rgba(0,255,0,0.3),
        rgba(255,255,0,0.3),
        rgba(0,170,255,0.3),
        rgba(255,0,0,0.3)
    );
    background-size: 400% 400%;
    animation: gradientBG 6s linear infinite;
    color: #ecf0f1;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}



    /* Glowing main title */
.main-title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
    background: linear-gradient(
        270deg,
        rgba(255,75,43,1),  /* Red */
        rgba(255,0,0,1)     /* Darker Red */
    );
    background-size: 800% 800%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 
        0 0 4px rgba(255,75,43,0.6),
        0 0 8px rgba(255,0,0,0.6);
    animation: luminousFlow 6s linear infinite;
}

@keyframes luminousFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}


@keyframes luminousFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}




    /* Movie cards */
    .movie-card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 20px;
    }
.movie-card {
    display: inline-block;
    background: #2c3e50; /* professional dark background */
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

/* Hover effect: glowing gradient flow */
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
}




    /* Subheader */
    .custom-subheader {
        text-align: center;
        font-size: 28px;
        font-weight: 600;
        color: #ecf0f1;
        margin-top: 20px;
    }

    /* Responsive adjustments */
    @media (max-width: 600px) {
        .movie-card { width: 90%; }
        .main-title { font-size: 40px; }
        .custom-subheader { font-size: 24px; }
    }
    </style>
""", unsafe_allow_html=True)

# ---- Title ----
st.markdown("<div class='main-title'> Movie Recommendation System</div>", unsafe_allow_html=True)

# ---- Search box ----
# Display as H2 heading
st.markdown("<h3 style='text-align: center; color: #ecf0f1;'>Search your favorite movie 🎥</h3>", unsafe_allow_html=True)

# Then render the selectbox without label
selected_movie_name = st.selectbox('', movies.title.values, key='movie_select')


def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similars[movie_idx]
    e_distances = list(enumerate(distances))
    similar = sorted(e_distances, reverse=True, key=lambda x: x[1])[1:11]
    return [movies.iloc[i[0]].title for i in similar]

# ---- Recommend button ----
if st.button('✨ Recommend'):
    recommendations = recommend(selected_movie_name)
    st.markdown("<div class='custom-subheader'>🔥 Top Recommendations for You:</div>", unsafe_allow_html=True)

    # Wrap all cards in a single container
    movie_cards = "<div class='movie-card-container'>"
    for rec in recommendations:
        movie_cards += "<div class='movie-card'>🎬<div class='movie-title'>{}</div></div>".format(rec)
    movie_cards += "</div>"

    # Render all cards at once
    st.markdown(movie_cards, unsafe_allow_html=True)


