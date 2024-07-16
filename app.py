import streamlit as st
from model import load_sentiment_model, predict_sentiment

# Load the model once when the app starts
model = load_sentiment_model()

st.title("Sentiment Analysis Web App")
st.write("Enter a sentence to analyze its sentiment (up to 50 words):")

# Function to count words
def count_words(text):
    return len(text.split())

# Maximum words allowed
max_words = 50

# Function to reset text area
def reset_input():
    st.session_state.user_input = ""

# Text input area with session state
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

user_input = st.text_area("Text Input", st.session_state.user_input, key="user_input")

# Display real-time word count
word_count = count_words(user_input)
st.write(f"Total word count: {word_count}/{max_words}")

# Create columns for the buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("Submit"):
        if word_count == 0:
            st.write("Please enter some text.")
        elif word_count > max_words:
            st.write(f"Text is too long. You entered {word_count} words. Please limit your input to {max_words} words.")
        else:
            # Predict sentiment
            results = predict_sentiment(model, user_input)
            for result in results:
                st.write(f"Sentiment: {result['label']} & Confidenece Score: {result['score']:.4f}")

with col2:
    st.button("Reset", on_click=reset_input)