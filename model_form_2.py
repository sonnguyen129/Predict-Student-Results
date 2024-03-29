import matplotlib
import streamlit as st
from src.model import get_prediction
import numpy as np
import pandas as pd
# import shap
import os
import pickle
# from pickle import load, dump
import matplotlib.pyplot as plt
from PIL import Image
from xgboost import XGBClassifier
import plotly.graph_objs as go

curr_path = os.path.dirname(os.path.realpath(__file__))

options_Major = ['Hệ thống thông tin quản lý', 'Kinh doanh quốc tế', 'Kế toán doanh nghiệp', 
                 'Luật kinh tế', 'Ngân hàng', 'Ngôn ngữ Anh', 'Nhóm ngành Quản trị', 'Tài chính']
options_Gender = ['Nam', 'Nữ']
options_GroupID = ['0', '1', '3', '4', '5', '6', '7']
options_Region = ['1', '2', '2NT', '3']
options_AdmissionCode = ['A00', 'A01', 'C00', 'D01', 'D07', 'D09']

def app():
    st.markdown("<h2 align='center'>Dự đoán kết quả tốt nghiệp</h2>", unsafe_allow_html=True)
    with st.form("Dự đoán kết quả tốt nghiệp"):
        # form header
        st.subheader("Nhập dữ liệu để tiến hành dự đoán:")
        # input elements
        major = st.selectbox("Khoa: ", options = options_Major)
        gender = st.selectbox("Giới tính: ", options = options_Gender)
        groupid = st.selectbox("Đối tượng xét tuyển: ", options = options_GroupID)
        region = st.selectbox("Khu vực: ", options = options_Region)
        admissioncode = st.selectbox("Khối xét tuyển: ", options = options_AdmissionCode)
        entrancescore = st.slider("Điểm thi THPTQG: ", min_value=0.0, max_value=30.0, step=0.25, value=20.0)
        creditsearned1 = st.slider("Số tín chỉ tích lũy ở kì đầu tiên: ", min_value=0, max_value=24, step=1, value=18)
        creditsearned2 = st.slider("Số tín chỉ tích lũy ở kì thứ 2: ", min_value=0, max_value=24, step=1, value=18)
        creditsearned3 = st.slider("Số tín chỉ tích lũy ở kì thứ 3: ", min_value=0, max_value=24, step=1, value=18)
        creditsearned4 = st.slider("Số tín chỉ tích lũy ở kì thứ 4: ", min_value=0, max_value=24, step=1, value=18)
        gpa1 = st.number_input('Điểm trung bình ở kì học đầu tiên (Làm tròn 2 chữ số sau dấu phẩy): ')
        gpa2 = st.number_input('Điểm trung bình ở kì học thứ 2 (Làm tròn 2 chữ số sau dấu phẩy): ')
        gpa3 = st.number_input('Điểm trung bình ở kì học thứ 3 (Làm tròn 2 chữ số sau dấu phẩy): ')
        gpa4 = st.number_input('Điểm trung bình ở kì học thứ 4 (Làm tròn 2 chữ số sau dấu phẩy): ')

        # submitting values
        submit_val = st.form_submit_button("Kết quả")
        if submit_val:
            # list of features
            feats = ['Major', 'Gender', 'GroupID', 'Region', 'AdmissionCode',
                     'EntranceScore', 'CreditsEarnned1', 'CreditsEarnned2', 'CreditsEarnned3', 
                     'CreditsEarnned4', 'GPA1', 'GPA2', 'GPA3', 'GPA4']
            # with open('model/features.pickle', 'wb') as f:
            #     pickle.dump(feats, f)
            # list of corresponding input values
            attribute_vals = [major, gender, groupid, region, admissioncode,
                              entrancescore, creditsearned1, creditsearned2, creditsearned3,
                              creditsearned4, gpa1, gpa2, gpa3, gpa4]
            
            # dictionary of features and values
            attr_dict = dict(zip(feats, attribute_vals))
            # dataframe for scaling and model input
            attr_df = pd.DataFrame(attr_dict, index=[1])
        
            # transform
            # preprocessor = load(open('model/preprocessor.pkl', 'rb'))
            with open('weights/model_2/preprocessor.pkl', 'rb') as file:
                preprocessor = pickle.load(file) 

            # model = XGBClassifier()
            with open('weights/model_2/model_best.pkl', 'rb') as f:
                model = pickle.load(f) # importing model to predict

            X = preprocessor.transform(attr_df)

            # predicted value from the model
            pred = get_prediction(model, X)

            pred_value = np.round(pred.squeeze() * 100, 2)
            target = ['Tốt nghiệp Giỏi', 'Tốt nghiệp Khá', 'Tốt nghiệp Trung bình', 'Tốt nghiệp Xuất sắc']
            
            # results header
            st.header("Kết quả dự đoán: ")
            # output results
            # st.success(f"Kết quả tốt nghiệp dự đoán: {pred}")

            with st.container():
                fig = go.Figure(data=[go.Bar(x = target, y = pred_value)])
        
                # add labels and title
                fig.update_layout(
                    title = 'Khă năng tốt nghiệp',
                    # xaxis_title='Categories',
                    yaxis_title = 'khả năng'
                )
                
                # display the plot
                st.plotly_chart(fig)
            
            # st.markdown('---')
    
