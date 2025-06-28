# 🧠 Myntra Review Sentiment Classifier

This project is an end-to-end machine learning pipeline to classify Myntra product reviews into **Positive**, **Neutral**, or **Negative** sentiments. It includes scraping, exploratory data analysis (EDA), model training, and serving predictions via a **FastAPI** API.

🔗 **Live API**: [https://myntra-sentiment.onrender.com/docs](https://myntra-sentiment.onrender.com/docs#/)

---

## ✅ Overview

1. **Scrapes product reviews** from Myntra using Selenium.
2. **Cleans and preprocesses** the reviews using NLTK.
3. **Performs EDA and visualization** in a Jupyter Notebook to understand data distribution and sentiment patterns.
4. **Trains a sentiment classifier** using Logistic Regression.
5. **Handles class imbalance** using SMOTE.
6. **Saves trained model and vectorizer** as `.pkl` files.
7. **Provides a FastAPI endpoint** to predict the sentiment of a given review.
8. **Deployed online** via Render — available for live predictions.

---

## 🗂️ Project Structure
├── app.py
├── scrape.py
├── EDA.ipynb
├── clean_and_prepare.py
├── train_model.py
├── logreg_sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
└── README.md


## 🚀 How to Use This Project

### 1. Clone the Repo
```
git clone https://github.com/yourusername/myntra-sentiment.git
cd myntra-sentiment
```
### 2. Install Dependencies
```
python -m venv venv
source venv/bin/activate    # on Linux/Mac
venv\Scripts\activate       # on Windows

pip install -r requirements.txt
```
### 3. Scrape Reviews from Myntra
```
python scrape.py
```
### 4. Explore and Train
* Open EDA.ipynb to:
* Explore rating and review length distributions

* Map ratings to sentiments (Positive, Neutral, Negative)

* Clean text (remove punctuation, stopwords, stemming)

* Handle imbalance using SMOTE

* Train models and evaluate performance

* Save final model and vectorizer

### 5. Serve the Model Locally
```
uvicorn app:app --reload
```
