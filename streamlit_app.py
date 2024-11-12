import pandas as pd
import re
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
from textblob import TextBlob
import cleantext 
st.title("Ứng Dụng Phân Tích Cảm Xúc")

# Sử dụng file_uploader để tải tệp CSV
with st.expander('Analyze Text'):
        text = st.text_input ('Text here: ')
        if text: 
                blob = TextBlob(text) 
                st.write('Tích cực: ', round(blob.sentiment.polarity, 2))
                st.write('Tiêu cực: ', round(blob.sentiment.subjectivity, 2))


