import streamlit as st
from src.multipage import MultiPage
import model_form_1
import model_form_2
import model_form_3
from src import explain_model
from PIL import Image

# page settings
st.set_page_config(page_title="Dự đoán tốt nghiệp quá hạn",
                page_icon="🎓",
                layout="wide")

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# image = Image.open("images/Logo_HVNH.png")
# st.image(image, width= 150, align='center')
# st.markdown("<h1 align='center'> 🎓 Ứng dụng dự đoán sinh viên có nguy cơ tốt nghiệp quá hạn </h1>", unsafe_allow_html=True)
# st.image("images/background.jpg", use_column_width=True)

left_co, last_co = st.columns([1,4])
with left_co:
    st.image("images/Logo_HVNH.png", width= 120)
with last_co:
    st.markdown("<h1 align='center'> 🎓 Ứng dụng dự đoán sinh viên có nguy cơ tốt nghiệp quá hạn </h1>", unsafe_allow_html=True)

st.sidebar.title("App Navigation")
# Add all your applications (pages) here
app.add_page("Giới thiệu", explain_model.app)
app.add_page("Dự đoán nguy cơ tốt nghiệp quá hạn", model_form_1.app)
app.add_page("Dự đoán kết quả tốt nghiệp", model_form_2.app)
app.add_page("Dự đoán nguy cơ tốt nghiệp quá hạn và buộc thôi học", model_form_3.app)

# The main app
app.run()