from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from emoji_data import sentiment_emojis, keyword_emojis

analyzer = SentimentIntensityAnalyzer()

def analyze_text_to_emoji(text):
    """
    Analyze sentiment using both TextBlob and VADER,
    combine both scores, and return best-fitting emojis.
    """

    # TextBlob sentiment
    blob_score = TextBlob(text).sentiment.polarity

    # VADER sentiment
    vader_score = analyzer.polarity_scores(text)["compound"]

    # Average sentiment score
    final_score = round((blob_score + vader_score) / 2, 3)

    if final_score > 0.5:
        sentiment_label = "very_positive"
    elif final_score > 0.1:
        sentiment_label = "positive"
    elif final_score < -0.5:
        sentiment_label = "very_negative"
    elif final_score < -0.1:
        sentiment_label = "negative"
    else:
        sentiment_label = "neutral"

    # Start with sentiment-based emojis
    emojis = sentiment_emojis[sentiment_label]

    # Keyword mapping
    words = text.lower().split()
    for word in words:
        if word in keyword_emojis:
            emojis.extend(keyword_emojis[word])

    # Deduplicate and return
    unique_emojis = list(dict.fromkeys(emojis))[:10]
    return unique_emojis, final_score
