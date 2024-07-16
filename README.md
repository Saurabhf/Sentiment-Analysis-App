# Sentiment Analysis Web App

This repository contains a simple web application for sentiment analysis using the `transformers` library and the `Streamlit` framework. The app allows users to input a sentence and get its sentiment (positive or negative) with a confidence score.

## Features

- **Sentiment Analysis**: The app uses the `distilbert/distilbert-base-uncased-finetuned-sst-2-english` model from Hugging Face's `transformers` library to perform sentiment analysis.
- **Real-time Word Count**: The app displays the word count of the input text and limits the input to a maximum of 50 words.
- **Reset Functionality**: Users can reset the input text area using the reset button.

## Code Overview

### `model.py`

- **`load_sentiment_model()`**: Loads the sentiment analysis model from the `transformers` library.
- **`predict_sentiment(model, text)`**: Takes the model and input text as arguments and returns the sentiment prediction.

### `app.py`

- Loads the sentiment analysis model when the app starts.
- Provides a text input area for users to enter a sentence (up to 50 words).
- Displays the word count in real-time.
- Provides "Submit" and "Reset" buttons to analyze the sentiment or reset the input, respectively.
- Shows the sentiment and confidence score upon submission.

## Usage

1. Enter a sentence in the text input area.
2. Check the word count to ensure it does not exceed 50 words.
3. Click the "Submit" button to get the sentiment analysis results.
4. Click the "Reset" button to clear the input area.

## Dependencies

- `transformers`: For the sentiment analysis model.
- `streamlit`: For building the web app interface.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
