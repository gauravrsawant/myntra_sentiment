import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn import preprocessing
import nltk
nltk.download('stopwords')

STOPWORDS = set(stopwords.words('english'))
stemmer = PorterStemmer()

def load_reviews(path="myntra_reviews.json"):
    import json
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data["reviews"])[["rating", "review"]]
    df["review"].replace("", pd.NA, inplace=True)
    df.dropna(subset=["review"], inplace=True)
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").astype("Int64")
    return df.dropna(subset=["rating"])

def map_rating(r):
    if r in [4, 5]:
        return "Positive"
    elif r == 3:
        return "Neutral"
    else:
        return "Negative"

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    text = [stemmer.stem(word) for word in text if word not in STOPWORDS]
    return ' '.join(text)

def prepare_data(df):
    df["category"] = df["rating"].apply(map_rating)
    le = preprocessing.LabelEncoder()
    df["sentiment"] = le.fit_transform(df["category"])
    df["cleaned_review"] = df["review"].apply(clean_text)
    return df
