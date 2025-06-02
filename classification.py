import joblib

def predict_category(text):
    vectorizer = joblib.load("vectorizer.joblib")
    model = joblib.load("classifier.joblib")
    X = vectorizer.transform([text])
    return model.predict(X)[0]