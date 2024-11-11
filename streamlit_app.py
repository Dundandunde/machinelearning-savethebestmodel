import streamlit as st
st.title('🎈 Learning')
st.write('Hello world!')

# Tiêu đề của ứng dụng
st.title("Tải dữ liệu CSV lên Streamlit")

# Hướng dẫn tải tệp
st.write("Vui lòng tải lên tệp CSV của bạn:")

# Sử dụng file_uploader để tải tệp CSV
uploaded_file = st.file_uploader("Chọn tệp CSV", type=["csv"])

# Kiểm tra nếu tệp đã được tải lên
if uploaded_file is not None:
    try:
        # Đọc tệp CSV từ dữ liệu đã tải lên bằng pandas
        df = pd.read_csv(uploaded_file)
        
        # Hiển thị dữ liệu dưới dạng bảng
        st.write("Dữ liệu đã tải lên:")
        st.dataframe(df)  # Dùng st.dataframe thay vì st.write để hiển thị bảng đẹp hơn
        
        # Hiển thị thông tin mô tả của dữ liệu
        st.write("Thông tin mô tả của dữ liệu:")
        st.write(df.describe())
        
        # Kiểm tra kiểu dữ liệu của các cột
        st.write("Kiểu dữ liệu của các cột:")
        st.write(df.dtypes)

    except Exception as e:
        st.error(f"Đã xảy ra lỗi khi đọc tệp CSV: {e}")
else:
    st.write("Vui lòng tải lên một tệp CSV.")

