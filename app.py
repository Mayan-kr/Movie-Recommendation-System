import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
@st.cache_data
def load_data():
    df = pd.read_csv("netflix_titles.csv")
    df = df[df['type'] == 'Movie']
    df = df.dropna(subset=['title', 'description', 'listed_in', 'cast', 'release_year'])  # 💥 Now includes cast & year
    df = df.reset_index(drop=True)
    df['combined_features'] = df['listed_in'] + " " + df['description']
    return df

@st.cache_resource
def compute_similarity(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined_features'])
    similarity_matrix = cosine_similarity(tfidf_matrix)
    return similarity_matrix

# Recommender logic
def recommend_movie(title, df, similarity_matrix, top_n=5):
    title_lower = title.strip().lower()
    matches = df[df['title'].str.strip().str.lower() == title_lower]
    if matches.empty:
        return None, []

    idx = matches.index[0]
    similarity_scores = list(enumerate(similarity_matrix[idx]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    recommendations = []
    count = 0
    for i in sorted_scores:
        if i[0] == idx:
            continue
        if count >= top_n:
            break
        row = df.iloc[i[0]]
        movie_info = {
            'Title': row['title'],
            'Description': row['description'],
            'Genres': row['listed_in'],
            'Cast': row['cast'],
            'Release Year': row['release_year']
        }
        recommendations.append(movie_info)
        count += 1

    input_movie = {
        'Title': df.iloc[idx]['title'],
        'Description': df.iloc[idx]['description'],
        'Genres': df.iloc[idx]['listed_in'],
        'Cast': df.iloc[idx]['cast'],
        'Release Year': df.iloc[idx]['release_year']
    }

    return input_movie, recommendations

# UI Setup
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎥 Netflix Movie Recommender")
st.write("Find movies similar to your favorite one using content-based filtering!")

df = load_data()
similarity_matrix = compute_similarity(df)

movie_title = st.text_input("Enter a movie title:")

if movie_title:
    input_movie, recommendations = recommend_movie(movie_title, df, similarity_matrix)

    if input_movie:
        st.subheader("🎯 You Searched For:")
        st.markdown(f"**{input_movie['Title']}** ({input_movie['Release Year']})")
        st.write(input_movie['Description'])
        st.write(f"🎭 *Genres:* {input_movie['Genres']}")
        st.write(f"🎬 *Cast:* {input_movie['Cast']}")

        st.subheader("🎁 Recommendations:")
        for rec in recommendations:
            st.markdown(f"**{rec['Title']}** ({rec['Release Year']})")
            st.write(rec['Description'])
            st.write(f"🎭 *Genres:* {rec['Genres']}")
            st.write(f"🎬 *Cast:* {rec['Cast']}")
            st.markdown("---")
    else:
        st.error("Movie not found 💔 Try checking the title and try again.")
