from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer

# TEXT PROCESSING

# example keywords for testing purposes
keywords = ['died', 'water', 'cat', 'room', 'house', 'spoke', 'falling', 'sky']

# get keywords
def extract(text):
    tokens = word_tokenize(text.lower())
    matches = [key for key in tokens if key in keywords]
    
    return matches

# test
dream_text = input("Enter your dream: ")

extracted = extract(dream_text)
print(extracted)

analyzer = SentimentIntensityAnalyzer()

# sentiment anayliss of text
def sentiment_analysis(text):

    score = analyzer.polarity_scores(text)

    if score > 0.05:
        return 'pos'
    elif score < -0.05:
        return "neg"
    else:
        return "nuetral"
    
vectorizer = TfidfVectorizer()

