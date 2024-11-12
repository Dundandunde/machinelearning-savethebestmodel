from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext 
st.title("Ứng Dụng Phân Tích Cảm Xúc")

# Sử dụng file_uploader để tải tệp CSV
with st.expander('Analyze Text'):
        text = st.text_input ('Text here: ')
        if text: 
                blob = TextBlob(text) 
                st.write('Tích cực: ', round(blob.sentiment.polarity, 2))
                st.write('Tiêu cực: ', round(blob.sentiment.subjectivity, 2))


