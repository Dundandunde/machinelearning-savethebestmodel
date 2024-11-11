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
            # Vector hóa dữ liệu văn bản
            vectorizer = TfidfVectorizer(min_df=1)
            train_data,test_data = train_test_split(df,train_size=0.8,random_state=0)
            X_train = vectorizer.fit_transform(train_data['review'])
            y_train = train_data['Sentiment']
            X_test = vectorizer.transform(test_data['review'])  
            y_test = test_data['Sentiment']
            
           # Bước 3: Huấn luyện mô hình Logistic Regression
            model =  BernoulliNB()
            model.fit(X_train, y_train)
            
            # Bước 4: Dự đoán và đánh giá mô hình
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            st.write(f"Độ chính xác của mô hình: {accuracy * 100:.2f}%")

            # Lưu mô hình và vectorizer
            joblib.dump(model, 'sentiment_model.pkl')
            joblib.dump(vectorizer, 'vectorizer.pkl')
            st.write("Mô hình và vectorizer đã được lưu thành công.")
        else:
            st.write("Dữ liệu cần có các cột 'review' và 'Sentiment'.")

st.header("Phân Tích Cảm Xúc Văn Bản Mới")

# Người dùng nhập văn bản để phân tích cảm xúc
text_input = st.text_area("Nhập văn bản cần phân tích cảm xúc", "Ví dụ: Tôi yêu ứng dụng này!")

if st.button('Phân tích cảm xúc'):
    # Kiểm tra nếu mô hình đã được tải
    if 'sentiment_model.pkl' in locals() and 'vectorizer.pkl' in locals():
        # Tải mô hình và vectorizer đã lưu
        model = joblib.load('sentiment_model.pkl')
        vectorizer = joblib.load('vectorizer.pkl')
        
        # Chuyển văn bản thành vector số
        text_vectorized = vectorizer.transform([text_input])
        
        # Dự đoán cảm xúc
        sentiment = model.predict(text_vectorized)
        
        # Hiển thị kết quả dự đoán
        if sentiment == 1:
            st.write("Cảm xúc: Tích cực 😃")
        elif sentiment == 0:
            st.write("Cảm xúc: Trung tính 😐")
        else:
            st.write("Cảm xúc: Tiêu cực 😞")
    else:
        st.write("Chưa có mô hình hoặc vectorizer đã huấn luyện.")
