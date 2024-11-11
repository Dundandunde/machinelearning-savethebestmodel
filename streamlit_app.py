import streamlit as st
st.title('🎈 Machine Learning')
st.write('Hello world!')

url = 'https://drive.google.com/file/d/16uecFM3ENg5sfdCBNk8xqcX79j3CVKiX/view?usp=drive_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
data = pd.read_csv(url, encoding='unicode_escape')

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
