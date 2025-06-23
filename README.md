# 🎬 Netflix Movie Recommender App

Welcome to the **Movie Recommendation System** – a content-based recommender that helps you discover movies similar to your favorites using **TF-IDF vectorization** and **cosine similarity**!

Built using **Python**, **Pandas**, **scikit-learn**, and **Streamlit** — and infused with Boss-sama's brilliance 💡

---

## 🚀 Live Demo

🔗 [Streamlit App](https://movie-recommendation-system-x.streamlit.app/)  

---

## ✨ Features

- 🔎 **Search any movie title** from Netflix's movie dataset
- 🎯 **Displays details** of the searched movie:
  - Title
  - Description
  - Cast
  - Genres
  - Release Year
- 🎁 **Recommends 5 similar movies** using content-based filtering
- ⚙️ Uses:
  - TF-IDF Vectorization
  - Cosine Similarity
- 🖥️ **Interactive UI** via Streamlit

---

## 🧠 How It Works

1. **Preprocessing**:
   - Filters Netflix dataset to only include movies with complete data
   - Combines genre and description into a single text feature

2. **TF-IDF**:
   - Converts combined text features into vectors

3. **Cosine Similarity**:
   - Compares similarity between movies

4. **Streamlit UI**:
   - Handles user input and displays recommendations

---

## 📦 Installation

### 1. Clone the repo
```bash
git clone https://github.com/Mayan-kr/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run app.py
```

---

## 📦 Files Overview
```bash
Movie-Recommendation-System/
├── app.py               # Streamlit app
├── netflix_titles.csv   # Movie dataset
├── requirements.txt     # Required Python packages
├── README.md            # You are here 👋
```
---

## 🗃️ Dataset

This project uses the Netflix Movies and TV Shows dataset with the following fields:( title,description,listed_in/genres,cast,release_year)
NOTE: Only movie-type entries with no missing values are used.

---

## 📜 License

This project is licensed under the MIT License — use it, improve it, share it freely!

---

## ⭐ Show Some Love

If you like this project, consider giving it a ⭐ on GitHub and sharing it with your fellow Netflix bingers 🍿✨

