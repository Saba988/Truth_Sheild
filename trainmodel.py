import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

# Step 1: Load the datasets
print("📥 Loading data...")
fake = pd.read_csv("C:/Users/FCC/.cache/kagglehub/datasets/clmentbisaillon/fake-and-real-news-dataset/versions/1/Fake.csv")
true = pd.read_csv("C:/Users/FCC/.cache/kagglehub/datasets/clmentbisaillon/fake-and-real-news-dataset/versions/1/True.csv")



fake["label"] = "FAKE"
true["label"] = "REAL"

df = pd.concat([fake, true])
df = df[["text", "label"]]

print("✅ Data loaded successfully!")

# Step 2: Split the data
print("📊 Splitting data into train and test sets...")
x_train, x_test, y_train, y_test = train_test_split(df["text"], df["label"], test_size=0.25, random_state=42)

# Step 3: Convert text to numbers
print("🔤 Converting text to numbers using TF-IDF...")
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
x_train_tfidf = vectorizer.fit_transform(x_train)
x_test_tfidf = vectorizer.transform(x_test)

# Step 4: Train the model
print("🤖 Training the Passive Aggressive Classifier model...")
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(x_train_tfidf, y_train)

print("✅ Model trained successfully!")

# Step 5: Save the model and vectorizer
print("💾 Saving model and vectorizer...")

joblib.dump(model, "fake_news_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("✅ Model and vectorizer saved as:")
print("📁 fake_news_model.pkl")
print("📁 tfidf_vectorizer.pkl")

# Step 6: Done
print("🎉 Training complete! You're ready to detect fake news!")
