import streamlit as st
from PIL import Image

def app():
    st.markdown("<h2 align='center'>Giới thiệu</h2>", unsafe_allow_html=True)

    st.write("""
    Dữ liệu được thu thập của 6.696 sinh viên Khoa Ngân hàng hệ đại học chính quy thuộc Học viện Ngân hàng, 
    Hà Nội, Việt Nam thuộc các học kỳ năm học từ 2010-2020.
    Dữ liệu bao gồm các thuộc tính về đặc điểm nhân khẩu học và các thông tin học thuật trong quá trình học của sinh viên.
    Dữ liệu được thu thập qua cơ sở dữ liệu phần mềm quản lý đào tạo của Học viện Ngân hàng. 
    """)
    
    st.markdown("<h2 align='center'>Thông tin dữ liệu đầu vào của mô hình</h2>", unsafe_allow_html=True)
    
    st.markdown("""


    | Feature | Loại dữ liệu | Mô tả |
    | :---------: | :-----------------: | :----: |
    | StudentID | Categorical | Mã số sinh viên |
    | Major | Categorical | Ngành học |
    | Gender | Categorical | Giới tính |
    | GroupID | Categorical | Đối tượng xét tuyển |
    | Region | Categorical | Khu vực |
    | AdmissionCode | Categorical | Khối xét tuyển |
    | Entrance Score | Numerical | Điểm thi THPTQG |
    | CreditsEarned1 | Numerical | Số tín chỉ tích lũy ở kì đầu tiên |
    | CreditsEarned2 | Numerical | Số tín chỉ tích lũy ở kì thứ 2 |
    | CreditsEarned3 | Numerical | Số tín chỉ tích lũy ở kì thứ 3 |
    | CreditsEarned4 | Numerical | Số tín chỉ tích lũy ở kì thứ 4 |
    | GPA1 | Numerical | Điểm trung bình ở kì học đầu tiên |
    | GPA2 | Numerical | Điểm trung bình ở kì học thứ 2 |
    | GPA3 | Numerical | Điểm trung bình ở kì học thứ 3 |
    | GPA4 | Numerical | Điểm trung bình ở kì học thứ 4 |
    """)
    st.markdown("---")

