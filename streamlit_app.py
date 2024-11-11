import streamlit as st
st.title('🎈 Learning')
st.write('Hello world!')

uploaded_file = st.file_uploader("/content/Womens Clothing E-Commerce Reviews.csv", type=["csv"])
if not (uploaded_file is None):
    df = pd.read_csv(uploaded_file)
    
    # Hiển thị dữ liệu dưới dạng bảng
    st.write(df)
