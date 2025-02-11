# Board Game Chatbot and Recommender

This project is a chatbot and recommender system for board games, developed using Streamlit, pandas, and scikit-learn. It helps users search for board games by name, get personalized recommendations based on a description, and explore various board game details.

---

## Features

### 1. **Search by Name**

Users can input the name of a board game, and the bot will return a list of matching board games along with their descriptions.

### 2. **Recommendations by Description**

Users can describe the type of board game they are interested in, and the bot will recommend games based on similarity.

### 3. **Board Game Information**

Retrieve detailed information about a board game, including:

- Name
- Description
- Thumbnail and Image URLs
- Ratings and Bayesian Ratings
- Number of Users Rated
- BGG Rank
- Standard Deviation of Ratings
- Owned, Trading, Wanting, and Wishing Counts
- Number of Weights and Average Weight
- Year Published
- Minimum and Maximum Players
- Playing Time, Minimum and Maximum Playtime
- Minimum Age

---

## How to Run the Application

### 1. Prerequisites

Ensure you have the following installed:

- Python 3.8+
- pip (Python package installer)

### 2. Install Dependencies

Run the following command to install all required libraries:

```bash
pip install -r requirements.txt
```

### 3. Download Dataset

Manually download the dataset from Kaggle:
[Kaggle Dataset](https://www.kaggle.com/datasets/caesuric/bgggamesdata)

Place the dataset in the appropriate directory before running the application.

### 4. Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

### 5. Interact with the Chatbot

Once the app is running, open the provided local URL in your web browser (e.g., `http://localhost:8501`) to start interacting with the chatbot.

---

## Dataset

The chatbot uses a dataset with the following columns:

| Column Name    | Description                            |
| -------------- | -------------------------------------- |
| `name`         | Name of the board game                 |
| `description`  | Detailed description of the board game |
| `thumbnail`    | URL to the thumbnail image             |
| `image`        | URL to the full image                  |
| `rating`       | Average rating                         |
| `bayes_rating` | Bayesian average rating                |
| `usersrated`   | Number of users who rated the game     |
| `bggrank`      | BoardGameGeek rank                    |
| `stddev`       | Standard deviation of ratings          |
| `owned`        | Number of users owning the game        |
| `trading`      | Number of users trading the game       |
| `wanting`      | Number of users wanting the game       |
| `wishing`      | Number of users wishing for the game   |
| `numweights`   | Number of users who rated complexity   |
| `averageweight`| Average complexity rating              |
| `yearpublished`| Year the game was published            |
| `minplayers`   | Minimum number of players              |
| `maxplayers`   | Maximum number of players              |
| `playingtime`  | Average playing time (minutes)         |
| `minplaytime`  | Minimum playing time (minutes)         |
| `maxplaytime`  | Maximum playing time (minutes)         |
| `age`          | Minimum recommended age                |

---

## Application Interface

Below is a Canva design showing the application in action:

[View Application Interface on Canva](https://www.canva.com/design/DAGeueGK-Fs/FYEiH1z8sMqvHMZHLPRaIw/view?utm_content=DAGeueGK-Fs&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=haabc22a8c4)

This interface allows users to:

- Search for games by name, description, player count, or playtime.
- View top-rated board games with recommendations.

---

## Contact Information

For questions, issues, or contributions, please contact:

**Email:** ariq.syas30@gmail.com

