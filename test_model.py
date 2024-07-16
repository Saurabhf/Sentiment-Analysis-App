from model import load_sentiment_model, predict_sentiment

# Load the model
model = load_sentiment_model()

# Analyze sentiment for a sample text
text = "Streamlit is awesome!"
results = predict_sentiment(model, text)
print(results)
