from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import re

# Hàm xử lý văn bản
def preprocess_text(text):
    if isinstance(text, str):  # Kiểm tra xem văn bản đầu vào có phải là chuỗi không
        text = re.sub(r'[^a-zA-Z\s]', '', text)  # Loại bỏ các ký tự không phải chữ và khoảng trắng
        text = cleantext.clean(text, clean_all=True)  # Làm sạch văn bản
        return text
    else:
        return ""  # Trả về chuỗi trống nếu không phải chuỗi văn bản

# Hàm phân tích cảm xúc
def score(x):
    blob1 = TextBlob(x)
    return blob1.sentiment.polarity

# Hàm phân loại cảm xúc
def analyze(x):
    if x >= 0.5:
        return 'Positive'
    elif x <= -0.5:
        return 'Negative'
    else:
        return 'Neutral'

# Giao diện người dùng trên Streamlit
st.header('Sentiment Analysis')

# Phân tích văn bản nhập vào
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        cleaned_text = preprocess_text(text)  # Tiền xử lý văn bản
        if cleaned_text:  # Kiểm tra xem văn bản đã được làm sạch hay không
            blob = TextBlob(cleaned_text)
            st.write('Điểm tích cực: ', round(blob.sentiment.polarity, 2))
            st.write('Điểm chủ quan: ', round(blob.sentiment.subjectivity, 2))
        else:
            st.warning("Văn bản nhập vào không hợp lệ hoặc quá ngắn.")

# Phân tích dữ liệu từ tệp CSV
with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')

    if upl:
        df = pd.read_csv(upl)

        # Kiểm tra và xử lý cột 'Review Text'
        if 'Review Text' in df.columns:
            # Loại bỏ các dòng có giá trị null hoặc NaN trong cột 'Review Text'
            df = df.dropna(subset=['Review Text'])
            
            # Đảm bảo tất cả giá trị trong cột 'Review Text' là chuỗi
            df['Review Text'] = df['Review Text'].apply(lambda x: str(x) if isinstance(x, (str, int, float)) else '')

            # Tiền xử lý văn bản trong cột 'Review Text'
            df['cleaned_review'] = df['Review Text'].apply(preprocess_text)
            
            # Áp dụng phân tích cảm xúc
            df['score'] = df['cleaned_review'].apply(score)
            df['analysis'] = df['score'].apply(analyze)
            st.write(df.head(10))
            
            # Chuyển đổi DataFrame thành CSV để tải xuống
            @st.cache
            def convert_df(df):
                return df.to_csv().encode('utf-8')

            csv = convert_df(df)

            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name='sentiment.csv',
                mime='text/csv',
            )
        else:
            st.error("Cột 'Review Text' không tồn tại trong tệp CSV!")
