import pandas as pd
import re
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
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

with st.expander('Tiền xử lý dữ liệu'):
        df.rename(columns={"Review Text": "review", "Rating" : "rating"}, inplace = True)
        df['review'] = df['review'].astype(str)  # Chuyển tất cả các giá trị thành chuỗi
        df = df.dropna(subset=['review'])  # Xóa các hàng có giá trị NaN trong cột 'review'
        df['review'] = df['review'].apply(clean_text)  # Loại bỏ ký tự đặc biệt
        st.write("Các cột trong dữ liệu: ", df.columns)
