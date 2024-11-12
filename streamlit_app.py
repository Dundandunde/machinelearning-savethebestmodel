from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext

st.header('Sentiment Analysis')
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Điểm tích cực: ', round(blob.sentiment.polarity,2))
        st.write('Điểm chủ quan: ', round(blob.sentiment.subjectivity,2))

    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all= False, extra_spaces=True ,
                                 stopwords=True ,lowercase=True ,numbers=True , punct=True))
