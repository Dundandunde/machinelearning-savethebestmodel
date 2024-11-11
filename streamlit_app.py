import streamlit as st
st.title('🎈 Machine Learning')
st.write('Hello world!')

url = 'https://drive.google.com/file/d/16uecFM3ENg5sfdCBNk8xqcX79j3CVKiX/view?usp=drive_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url, encoding='unicode_escape')
data.head(10)

def load_model(model_name):
    if model_name == 'Logistic Regression':
        return joblib.load('best_logistic_model.pkl')
    elif model_name == 'Naive Bayes':
        return joblib.load('best_naive_bayes_model.pkl')
    elif model_name == 'SVM':
        return joblib.load('best_svm_model.pkl')
    elif model_name == 'Random Forest':
        return joblib.load('best_random_forest_model.pkl')

# Giao diện người dùng Streamlit
st.title("Ứng Dụng Dự Đoán Mô Hình Học Máy")

# Chọn mô hình tốt nhất
model_choice = st.selectbox("Chọn mô hình", ['Logistic Regression', 'Naive Bayes', 'SVM', 'Random Forest'])

# Tải mô hình đã chọn
model = load_model(model_choice)

# Nhập giá trị đặc trưng từ người dùng
st.write("Nhập các giá trị đặc trưng (features):")

# Giả sử mô hình của bạn có 3 đặc trưng, ví dụ: feature1, feature2, feature3
feature1 = st.number_input("Feature 1", min_value=0.0, max_value=100.0, value=0.0)
feature2 = st.number_input("Feature 2", min_value=0.0, max_value=100.0, value=0.0)
feature3 = st.number_input("Feature 3", min_value=0.0, max_value=100.0, value=0.0)

# Tạo DataFrame cho các giá trị đặc trưng
input_data = np.array([[feature1, feature2, feature3]])
input_df = pd.DataFrame(input_data, columns=['Feature1', 'Feature2', 'Feature3'])

# Dự đoán khi người dùng nhấn nút
if st.button("Dự Đoán"):
    prediction = model.predict(input_df)
    st.write(f"Prediction: {prediction[0]}")
