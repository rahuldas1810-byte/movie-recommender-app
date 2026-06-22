# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using Machine Learning, Natural Language Processing (NLP), and Streamlit.

## 🚀 Live Demo



```text
https://movie-recommender-app97865434.streamlit.app/
```

---

## 📌 Features

* Recommend movies similar to a selected movie
* Content-based filtering approach
* Cosine Similarity for recommendation generation
* Interactive Streamlit web interface
* Supports 5000+ movies
* Fast recommendation retrieval

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* NLP
* Cosine Similarity

---

## ⚙️ How It Works

1. Movie metadata is preprocessed and cleaned.
2. Important features such as genres, cast, crew, keywords, and overview are combined.
3. Text data is vectorized using NLP techniques.
4. Cosine Similarity is calculated between movie vectors.
5. The top 5 most similar movies are recommended.

---

## 📂 Project Structure

```text
movie-recommender-app/
│
├── app.py
├── movie_dict.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🖥️ Run Locally

Clone the repository:

```bash
git clone https://github.com/rahuldas1810-byte/movie-recommender-app.git
```

Move to project directory:

```bash
cd movie-recommender-app
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit application:

```bash
streamlit run app.py
```

---

## 📊 Dataset

* TMDB 5000 Movies Dataset
* Movie metadata and credits datasets


 
 

⭐ If you found this project useful, consider giving it a star.
