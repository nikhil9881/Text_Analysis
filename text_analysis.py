import textblob
import spacy
from spacy import displacy

# Load the spaCy model for key phrase extraction
nlp = spacy.load("en_core_web_sm")

# Load the sample dataset of transcribed interview responses
with open(r"C:\Users\Dell\OneDrive\Desktop\New folder (2)\sample_response.txt") as f:
    responses = [line.strip() for line in f.readlines()]

# Define a function to analyze the sentiment of a response using TextBlob
def analyze_sentiment(response):
    blob = textblob.TextBlob(response)
    if blob.sentiment.polarity > 0:
        return "Positive"
    elif blob.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Define a function to extract key phrases from a response using spaCy
def extract_key_phrases(response):
    doc = nlp(response)
    key_phrases = [chunk.text for chunk in doc.noun_chunks]
    return key_phrases

expected_key_phrases = [
    "software development", "project management", "Python", "machine learning"
]

# Define a function to provide an overall quality assessment for a response
def quality_assessment(response):
    sentiment = analyze_sentiment(response)
    key_phrases = extract_key_phrases(response)
    
    relevance_score = sum(1 for phrase in key_phrases if phrase in expected_key_phrases)
    
    if sentiment == "Positive" and relevance_score > 0:
        return "Good"
    elif sentiment == "Neutral":
        return "Average"
    else:
        return "Needs Improvement"

# Analyze each response and output the results
for response in responses:
    sentiment = analyze_sentiment(response)
    key_phrases = extract_key_phrases(response)
    quality = quality_assessment(response)
    print(f"Response: {response}\nSentiment: {sentiment}\nKey Phrases: {key_phrases}\nQuality Assessment: {quality}\n")