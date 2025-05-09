import streamlit as st
import joblib
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Set Streamlit page configuration
st.set_page_config(page_title="TruthShield – AI Fake News Detector 🛡️", layout="wide", page_icon="🧠")

# Header section
st.markdown("""
    <h1 style='text-align: center; color: #00BFFF;'>🛡️ TruthShield – AI Fake News Detector</h1>
    <p style='text-align: center; color: #aaa;'>Helping you stay informed with real and trusted news 🧠</p>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📰 News Detector Menu")
choice = st.sidebar.radio("Choose Action", ["🧪 Detect News", "🌍 Global News"])

# Option 1: Detect Fake News
if choice == "🧪 Detect News":
    st.subheader("🧪 Enter a News Headline or Article")
    user_input = st.text_area("Paste any news content here:", height=200)
    if st.button("Check Truth 🧠"):
        if user_input.strip() != "":
            input_data = vectorizer.transform([user_input])
            prediction = model.predict(input_data)[0]
            if prediction == "FAKE":
                st.error("🚨 This news appears to be *Fake*. Please verify from official sources.")
            else:
                st.success("✅ This news appears to be *Real*.")
        else:
            st.warning("Please enter some text to check.")

# Option 2: Global News Feed
elif choice == "🌍 Global News":
    st.subheader("🌍 Real-time Global News (Powered by NewsAPI)")
    api_key = "68d6eafc678c4873862601d02c8130e6"  # Replace with your key
    query = st.text_input("Search for any topic (e.g., AI, war, economy):", value="world")

    if st.button("Fetch Latest News 🌐"):
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize=10&apiKey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:
            articles = response.json().get("articles", [])
            if articles:
                for article in articles:
                    st.markdown(f"""
                        <div style='border:1px solid #444;padding:10px;margin:10px;border-radius:10px;background-color:#111;color:#eee;'>
                            <h4>{article['title']}</h4>
                            <p>{article['description'] or 'No description available.'}</p>
                            <a href='{article['url']}' target='_blank'>🔗 Read more</a>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("No news found for this topic. Try a different one.")
        else:
            st.error("Failed to fetch news. Check your API key or internet connection.")

# Footer
st.markdown("""
    <hr style='margin-top:30px;'>
    <div style='text-align:center; color:gray;'>Built with ❤️ by Saba – Stay Aware, Stay Safe!</div>
""", unsafe_allow_html=True)
