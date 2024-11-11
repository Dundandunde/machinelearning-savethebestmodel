import streamlit as st

st.title('🎈 Machine Learning')
st.write('Hello world!')

# Hàm thu thập chỉ số đánh giá cho mỗi mô hình
def get_metrics(y_test, y_pred, model_name):
    report = mt.classification_report(y_test, y_pred, output_dict=True)
    return {
        'model': model_name,
        'precision': report['1']['precision'],
        'recall': report['1']['recall'],
        'f1-score': report['1']['f1-score']
    }

# Thu thập kết quả cho từng mô hình
results = [
    get_metrics(y_test, lr.predict(X_test), 'Logistic Regression'),
    get_metrics(y_test, nb.predict(X_test), 'Naive Bayes'),
    get_metrics(y_test, svc.predict(X_test), 'SVM'),
    get_metrics(y_test, rf.predict(X_test), 'Random Forest')
]

# Lưu vào DataFrame
df_results = pd.DataFrame(results)

# Tính điểm trung bình cho từng mô hình
df_results['mean_score'] = df_results[['precision', 'recall', 'f1-score']].mean(axis=1)

# Chọn mô hình tốt nhất (mô hình có điểm trung bình cao nhất)
best_model = df_results.loc[df_results['mean_score'].idxmax()]

# Streamlit giao diện
st.title("So sánh Mô Hình Học Máy")

# Hiển thị bảng kết quả
st.subheader("Bảng kết quả đánh giá của các mô hình")
st.dataframe(df_results)

# Hiển thị mô hình tốt nhất
st.subheader("Mô Hình Tốt Nhất")
st.write(f"**Mô hình tốt nhất là:** {best_model['model']}")
st.write(f"**Precision:** {best_model['precision']:.2f}")
st.write(f"**Recall:** {best_model['recall']:.2f}")
st.write(f"**F1-Score:** {best_model['f1-score']:.2f}")
st.write(f"**Mean Score:** {best_model['mean_score']:.2f}")
