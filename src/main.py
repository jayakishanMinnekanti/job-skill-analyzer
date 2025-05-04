# src/main.py
import os
import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report
from src.utils import clean_text, generate_labels, prepare_tfidf
from src.config import SKILL_LIST

# Create folders if not exist
os.makedirs("models", exist_ok=True)
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("data/data.csv")
df.dropna(subset=['Description'], inplace=True)

# Clean descriptions
df['clean_description'] = df['Description'].apply(clean_text)

# Generate multi-label binary matrix for skills
df = generate_labels(df, SKILL_LIST)

# Extract label matrix y and drop skills not found in any row
y = df[SKILL_LIST]
y = y.loc[:, (y.sum() > 0)]  # remove columns with 0s only

# Prepare TF-IDF matrix
X, tfidf = prepare_tfidf(df)

# Train the model
model = MultiOutputClassifier(LogisticRegression(max_iter=1000))
model.fit(X, y)

# Predict on training data
y_pred = model.predict(X)

# Classification report
print("\nClassification Report:\n")
print(classification_report(y, y_pred, target_names=y.columns.tolist()))

# Save the model and vectorizer
joblib.dump(model, "models/job_skill_model.pkl")
joblib.dump(tfidf, "models/tfidf.pkl")

# Plot Top 10 Predicted Skills
y_pred_df = pd.DataFrame(y_pred, columns=y.columns)
skill_counts = y_pred_df.sum().sort_values(ascending=False)
top_10 = skill_counts.head(10)

print("\nTop predicted skills:\n")
print(top_10)

plt.figure(figsize=(12, 6))
top_10.plot(kind='bar', color='dodgerblue')
plt.title("Top 10 Predicted In-Demand Skills from Job Descriptions")
plt.xlabel("Skill")
plt.ylabel("Number of Job Descriptions")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("images/top_10_skills_barplot.png")
plt.close()

# Heatmap of Skill Co-occurrence
top_10_skills = top_10.index.tolist()
top_10_co_matrix = y[top_10_skills].T.dot(y[top_10_skills])

plt.figure(figsize=(12, 10))
sns.heatmap(top_10_co_matrix, cmap="YlGnBu", linewidths=0.5, annot=True, fmt='d')
plt.title("Skill Co-occurrence Heatmap (Top 10 Predicted Skills)")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("images/top_10_skill_cooccurrence.png")
plt.close()

# WordCloud of all actual skill labels
actual_skill_counts = y.sum().sort_values(ascending=False)
wordcloud = WordCloud(width=1200, height=600, background_color='white').generate_from_frequencies(actual_skill_counts.to_dict())

plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Top Required Technical Skills (All Actual Labels)")
plt.tight_layout()
plt.savefig("images/top_skills_wordcloud.png")
plt.close()