import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("basic_data.csv")
    return df

df = load_data()

# Functions
def recommend_top_rated(df, top_n=5):
    """Recommend the top-rated board games."""
    top_rated = df.sort_values(by="rating", ascending=False).head(top_n)
    return top_rated[["name", "rating", "description", "image"]]

def search_by_name(query, df, vectorizer, top_n=5):
    """Search board games by name."""
    tfidf_matrix = vectorizer.fit_transform(df["name"].fillna("").astype(str))
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[top_indices][["name", "description", "image"]]

def get_recommendations(query, df, tfidf_matrix, vectorizer, top_n=1):
    """Get recommendations based on description."""
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = similarities.argsort()[-top_n:][::-1]
    return df.iloc[top_indices][["name", "description", "image"]]

def search_by_player_count(players, df, top_n=5):
    """Search board games that match the number of players."""
    filtered_df = df[(df["minplayers"] <= players) & (df["maxplayers"] >= players)]
    return filtered_df.sort_values(by="rating", ascending=False).head(top_n)

def search_by_playtime(time, df, top_n=5):
    """Search board games within a specific playing time range."""
    filtered_df = df[(df["minplaytime"] <= time) & (df["maxplaytime"] >= time)]
    return filtered_df.sort_values(by="rating", ascending=False).head(top_n)

def board_game_of_the_day(df):
    """Select a random board game as the game of the day."""
    random_index = random.randint(0, len(df) - 1)
    return df.iloc[random_index]

# Precompute TF-IDF matrix for descriptions
vectorizer_desc = TfidfVectorizer(stop_words='english')
tfidf_matrix_desc = vectorizer_desc.fit_transform(df["description"].fillna("").astype(str))

# Streamlit UI
st.title("Board Game Recommender & Information")

# Example Input Field
st.markdown("### Example Inputs")
st.markdown(
    """
    - **Search by Name**: `Catan`
    - **Recommendation by Description**: `A cooperative game about solving mysteries together.`
    - **Search by Players**: `2` (for games that support 2 players)
    - **Search by Playtime**: `60` (for games with a playing time of around 60 minutes)
"""
)

# Unified Input Field
user_input = st.text_input("Enter your query (e.g., name, description, player count, or playtime):")

if user_input:
    # Determine intent
    if user_input.isdigit():  # Check if input is a number (player count or playtime)
        players_or_time = int(user_input)
        if df[(df["minplayers"] <= players_or_time) & (df["maxplayers"] >= players_or_time)].empty is False:
            player_results = search_by_player_count(players_or_time, df)
            st.subheader(f"🎲 Games for {players_or_time} Players")
            for _, row in player_results.iterrows():
                st.write(f"**{row['name']}** (Rating: {row['rating']}): {row['description'][:150]}...")
                if not pd.isna(row["image"]):
                    st.image(row["image"], width=200)
        elif df[(df["minplaytime"] <= players_or_time) & (df["maxplaytime"] >= players_or_time)].empty is False:
            playtime_results = search_by_playtime(players_or_time, df)
            st.subheader(f"⏱️ Games with Playtime Around {players_or_time} Minutes")
            for _, row in playtime_results.iterrows():
                st.write(f"**{row['name']}** (Rating: {row['rating']}): {row['description'][:150]}...")
                if not pd.isna(row["image"]):
                    st.image(row["image"], width=200)
        else:
            st.write("No games found for the given input.")
    elif search_by_name(user_input, df, TfidfVectorizer(stop_words='english')).empty is False:  # Search by name
        search_results = search_by_name(user_input, df, TfidfVectorizer(stop_words='english'))
        st.subheader(f"🔎 Search Results for: {user_input}")
        for _, row in search_results.iterrows():
            st.write(f"**{row['name']}**: {row['description'][:150]}...")
            if not pd.isna(row["image"]):
                st.image(row["image"], width=200)
    else:  # Default to description-based recommendation
        recommendations = get_recommendations(user_input, df, tfidf_matrix_desc, vectorizer_desc)
        if not recommendations.empty:
            game = recommendations.iloc[0]
            st.subheader("🎯 Recommendation Based on Description")
            st.write(
                f"I recommend **{game['name']}**.\n\n"
                f"{game['description'][:200]}...\n\n"
                "Give it a try for an exciting experience!"
            )
            if not pd.isna(game["image"]):
                st.image(game["image"], width=300)
        else:
            st.write("Sorry, no recommendations found.")

# Feature: Top-Rated Games
st.subheader("⭐ Top-Rated Board Games")
top_n = st.slider("Number of recommendations", 1, 10, 5)
top_rated_games = recommend_top_rated(df, top_n)
for _, row in top_rated_games.iterrows():
    st.write(f"**{row['name']}** (Rating: {row['rating']}): {row['description'][:150]}...")
    if not pd.isna(row["image"]):
        st.image(row["image"], width=200)

# Feature: Board Game of the Day
st.subheader("🎲 Board Game of the Day")
if st.button("Show Today's Board Game"):
    daily_game = board_game_of_the_day(df)
    st.write(f"**{daily_game['name']}**\n\n{daily_game['description'][:200]}...")
    if not pd.isna(daily_game["image"]):
        st.image(daily_game["image"], width=300)
