import pickle

class FakeNewsDetector:
    def __init__(self, model_path, vectorizer_path):
        # Load the trained model
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        
        # Load the TF-IDF vectorizer
        with open(vectorizer_path, 'rb') as vectorizer_file:
            self.vectorizer = pickle.load(vectorizer_file)

    def predict(self, text):
        # Transform the input text using the loaded vectorizer
        text_vector = self.vectorizer.transform([text])
        
        # Predict using the loaded model
        prediction = self.model.predict(text_vector)
        
        # Return the prediction result
        return "Fake News 🚫" if prediction[0] == 0 else "Real News ✅"
