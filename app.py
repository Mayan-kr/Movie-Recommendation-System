import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df=pd.read_csv('netflix_titles.csv')
df = df[df['type'] == 'Movie']
df = df.dropna(subset=['title', 'description', 'listed_in'])
df = df.reset_index(drop=True)

df['combined_features'] = df['listed_in'] + ' ' + df['description']

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['combined_features'])

similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_movie(title, df, similarity_matrix, top_n=5):
    title_lower = title.lower()
    
    if title_lower not in df['title'].str.lower().values:
        return "Movie not found 💔 Try a different name."

    idx = df[df['title'].str.lower() == title_lower].index[0]

    similarity_scores = list(enumerate(similarity_matrix[idx]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Input movie (100% match)
    input_movie = {
        'Title': df.iloc[idx]['title'],
        'Description': df.iloc[idx]['description'],
        'Release Year': df.iloc[idx]['release_year'],
        'Cast': df.iloc[idx]['cast']
    }

    # Top N similar movies (excluding itself)
    similar_movies = []
    count = 0
    for i in sorted_scores:
        if i[0] == idx:
            continue  # Skip the input movie
        if count >= top_n:
            break
        movie_info = {
            'Title': df.iloc[i[0]]['title'],
            'Description': df.iloc[i[0]]['description'],
            'Release Year': df.iloc[i[0]]['release_year'],
            'Cast': df.iloc[i[0]]['cast']
        }
        similar_movies.append(movie_info)
        count += 1

    return {
        'Input Movie': input_movie,
        'Recommendations': similar_movies
    }
    
