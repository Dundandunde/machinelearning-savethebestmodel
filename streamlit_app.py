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
        if 'rating' in df.columns and 'review' in df.columns:
            # Chuyển giá trị số thành nhãn văn bản
            def rating_to_sentiment(rating):
                if rating >= 4:
                    return 'Tích cực'
                elif rating == 3:
                    return 'Trung tính'
                else:
                    return 'Tiêu cực'
