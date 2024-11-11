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

 with st.expander('Tiền xử lý dữ liệu'):  # Sửa tại đây
        if 'text' in df.columns and 'sentiment' in df.columns:
            # Vector hóa dữ liệu văn bản
            vectorizer = TfidfVectorizer(stop_words='english')
            X = vectorizer.fit_transform(df['text'])
            y = df['sentiment']
                
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
