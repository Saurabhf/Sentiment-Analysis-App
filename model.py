from transformers import pipeline

def load_sentiment_model():
    # Load the sentiment analysis pipeline
    model = pipeline(
        "text-classification",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
    )
    return model

def predict_sentiment(model, text):
    results = model(text)
    return results
