import streamlit as st
import pandas as pd
st.title("Ứng Dụng Phân Tích Cảm Xúc")
st.write('Hello world!')

# Sử dụng file_uploader để tải tệp CSV
with st.expander('Data'):
        uploaded_file = st.file_uploader("Chọn tệp CSV", type=["csv"])
        if uploaded_file is not None:
                df = pd.read_csv(uploaded_file)
                st.write("Dữ liệu đã tải lên:")
                df
                
                st.write('**Biến độc lập X**')
                X = df.drop(columns=["Rating"])
                X
                st.write('**Biến phụ thuộc Y**')
                Y = df.Rating
                Y

    # Bước 2: Tiền xử lý dữ liệu
with st.expander('Tiền xử lý dữ liệu'):
        if 'text' in df.columns and 'sentiment' in df.columns:
            vectorizer = TfidfVectorizer(stop_words='english')
            X = vectorizer.fit_transform(df['text'])
            y = df['sentiment']
           X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Bước 4: Huấn luyện mô hình Logistic Regression
            model = BernoulliNB()
            model.fit(X_train, y_train)
            
            # Dự đoán trên tập kiểm tra và tính độ chính xác
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")
            
            # Lưu mô hình và vectorizer
            joblib.dump(model, 'sentiment_model.pkl')
            joblib.dump(vectorizer, 'vectorizer.pkl')
            st.write("Mô hình và vectorizer đã được lưu thành công.")
        else:
            st.write("Dữ liệu cần có các cột 'text' và 'sentiment'.")
