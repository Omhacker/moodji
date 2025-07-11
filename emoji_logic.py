import re
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from emoji_data import sentiment_emojis, keyword_emojis
from nltk.stem import WordNetLemmatizer

analyzer = SentimentIntensityAnalyzer()
lemmatizer = WordNetLemmatizer()

def get_sentiment_label(score):
    if score > 0.5:
        return "very_positive"
    elif score > 0.1:
        return "positive"
    elif score < -0.5:
        return "very_negative"
    elif score < -0.1:
        return "negative"
    else:
        return "neutral"

def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    matched_emojis = []

    for word in words:
        lemma = lemmatizer.lemmatize(word)
        if lemma in keyword_emojis:
            matched_emojis.extend(keyword_emojis[lemma])

    return matched_emojis

def analyze_text_to_emoji(text):
    blob_score = TextBlob(text).sentiment.polarity
    vader_score = analyzer.polarity_scores(text)["compound"]
    final_score = round((blob_score + vader_score) / 2, 3)

    sentiment_label = get_sentiment_label(final_score)
    sentiment_based = sentiment_emojis.get(sentiment_label, [])

    keyword_based = extract_keywords(text)

    combined = list(dict.fromkeys(sentiment_based + keyword_based))[:8]
    return combined, final_score
