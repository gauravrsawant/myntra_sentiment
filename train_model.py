from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import joblib
from collections import Counter
from clean_and_prepare import load_reviews, prepare_data

df = load_reviews()
df = prepare_data(df)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
X = vectorizer.fit_transform(df["cleaned_review"])
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
smote = SMOTE(random_state=42)
X_res, y_res = smote.fit_resample(X_train, y_train)

model = LogisticRegression(max_iter=1000, class_weight="balanced", multi_class="multinomial")
model.fit(X_res, y_res)

y_pred = model.predict(X_test)
print("📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Negative", "Neutral", "Positive"]))

joblib.dump(vectorizer, "tfidf_vectorizer.pkl")
joblib.dump(model, "logreg_sentiment_model.pkl")
