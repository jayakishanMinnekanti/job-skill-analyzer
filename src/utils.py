# src/utils.py
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_text(text):
    """
    Clean raw job description text.
    """
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def generate_labels(df, skills):
    """
    Add binary columns indicating whether each skill is present in the text.
    """

    def label_skills(text):
        return [1 if skill in text else 0 for skill in skills]

    label_df = df['clean_description'].apply(lambda x: pd.Series(label_skills(x)))
    label_df.columns = skills
    return pd.concat([df, label_df], axis=1)


def prepare_tfidf(df):
    """
    Transform clean descriptions into TF-IDF matrix.
    """
    tfidf = TfidfVectorizer(max_features=1000, stop_words='english')
    X = tfidf.fit_transform(df['clean_description'])
    return X, tfidf