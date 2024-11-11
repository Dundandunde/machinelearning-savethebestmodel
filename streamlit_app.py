import streamlit as st
st.title('🎈 Machine Learning')
st.write('Hello world!')

url = 'https://drive.google.com/file/d/16uecFM3ENg5sfdCBNk8xqcX79j3CVKiX/view?usp=drive_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url, encoding='unicode_escape')
data.head(10)
