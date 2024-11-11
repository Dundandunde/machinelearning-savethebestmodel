import streamlit as st
import pandas as pd
st.title('🎈 Learning')
st.write('Hello world!')

# Sử dụng file_uploader để tải tệp CSV
uploaded_file = st.file_uploader("Chọn tệp CSV", type=["csv"])
if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Dữ liệu đã tải lên:")
        df
