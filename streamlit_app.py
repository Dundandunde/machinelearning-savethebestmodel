import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
import re
import nltk
# Giao diện người dùng trên Streamlit
st.header('Sentiment Analysis using Naive Bayes')

# Tải stopwords từ nltk
nltk.download('stopwords')
stop_words = stopwords.words('english')

#1. Các hàm tiền xử lý văn bản
def preprocess_text(text):
    if isinstance(text, str):                    #Kiểm tra xem văn bản đầu vào có phải là chuỗi không
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Loại bỏ ký tự không phải chữ và khoảng trắng
        text = text.lower()                      #Chuyển thành chữ thường
        text = re.sub(r'\s+', ' ', text)         #Loại bỏ khoảng trắng thừa
        text = ' '.join([word for word in text.split() if word not in stop_words])  #Loại bỏ stopwords
        return text
    else:
        return ""                               #Trả về chuỗi trống nếu không phải chuỗi văn bản

#2. Đọc dữ liệu từ file CSV
def load_data(file):
    df = pd.read_csv(file)
    if 'Review Text' in df.columns and 'Rating' in df.columns:
        df['cleaned_review'] = df['Review Text'].apply(preprocess_text)
        df['Sentiment'] = df['Rating'].apply(lambda x: 'Positive' if x >= 4 else ('Neutral' if x == 3 else 'Negative'))
        return df
    else:
        st.error("Cột 'Review Text' hoặc 'Rating' không tồn tại trong tệp CSV!")
        return None

#3. Các hàm huấn luyện mô hình Naive Bayes
def train_naive_bayes(df):
    X = df['cleaned_review']
    y = df['Sentiment']

    # Vector hóa văn bản thành ma trận đặc trưng
    vectorizer = CountVectorizer()
    X_vect = vectorizer.fit_transform(X)
    
    # Chia dữ liệu thành tập huấn luyện và kiểm tra
    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)

    # Huấn luyện mô hình Naive Bayes
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # Dự đoán trên tập kiểm tra
    y_pred = model.predict(X_test)

    # Đánh giá mô hình
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Độ chính xác của mô hình Naive Bayes: {accuracy * 100:.2f}%")

    return model, vectorizer

#4. Dự đoán cảm xúc của văn bản
def predict_sentiment(model, vectorizer, text):
    text = preprocess_text(text)  # Tiền xử lý văn bản
    text_vect = vectorizer.transform([text])  # Chuyển văn bản thành vector
    sentiment = model.predict(text_vect)
    return sentiment[0]

#5. Tải tệp CSV và huấn luyện mô hình
with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')
    
    if upl:
        df = load_data(upl)
        if df is not None:
            #Tiến hành huấn luyện mô hình Naive Bayes
            model, vectorizer = train_naive_bayes(df)
            st.write(df.head(10))

            #Bonus: Dự đoán cảm xúc cho văn bản mới (tự thêm)
            text = st.text_input('Enter text for sentiment prediction:')
            if text:
                sentiment = predict_sentiment(model, vectorizer, text)
                st.write(f"Predicted Sentiment: {sentiment}")
