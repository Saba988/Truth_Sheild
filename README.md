# 🛡️ TruthShield – AI Fake News Detector

> A real-time Fake News Detection System built using Python, Machine Learning, NLP, and Streamlit — empowering users to verify news accuracy with the help of artificial intelligence.

---

## 🚀 Project Overview

**TruthShield** is a smart web application that detects whether a news article or headline is fake or real using a machine learning model trained on real-world news datasets. It also fetches and displays real-time global news using the NewsAPI. The main goal of this project is to **combat misinformation**, especially in critical regions like India and Pakistan, by enabling users to validate news instantly.

---

## ✅ Key Features

- 🔍 **Fake News Detector**  
  Users can input any news text, and the app will analyze and classify it as either **Fake** or **Real** using a trained ML model.

- 🌐 **Live Global News Feed**  
  Integrated with NewsAPI to fetch up-to-date news articles based on the user's query.

- 👩‍💻 **Object-Oriented Python Code**  
  The backend and ML pipeline are structured using Object-Oriented Programming for modularity and reusability.

- 📊 **Machine Learning & NLP**  
  - TF-IDF Vectorizer  
  - PassiveAggressiveClassifier  
  - Custom pre-processing pipeline

- 💻 **Interactive UI with Streamlit**  
  A user-friendly, professional interface with options in the sidebar for switching between news detection and real-time news feed.

---

## 🧠 Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend:** Python (OOP)  
- **Libraries:** `pandas`, `scikit-learn`, `joblib`, `requests`, `streamlit`  
- **ML Model:** Passive Aggressive Classifier + TF-IDF  
- **News Source:** NewsAPI.org (Real-time fetching)

---

## 🔧 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TruthShield.git
   cd TruthShield
   
Install the required libraries:
pip install -r requirements.txt

Add your NewsAPI key in app.py:
api_key = "YOUR_NEWSAPI_KEY"

Run the app:
streamlit run app.py

---

# 🔒 Security Note
Your NewsAPI key should be kept private.

---

# 👤 Author
Saba Junaid – Computer Science Student & AI Enthusiast
“Stay Aware, Stay Safe!”
