import streamlit as st

# Define the multipage class to manage the multiple apps in our program 
class MultiPage: 
    def __init__(self) -> None:
        """Constructor with a list to store applications as an instance variable."""
        self.pages = []
    
    def add_page(self, title, func) -> None: 
        """Class Method to Add pages to the project"""
        self.pages.append({
                "title": title, 
                "function": func
            })

    def run(self):
        """Dropdown to select the page to run"""
        page = st.sidebar.selectbox(
            ' ', 
            self.pages, 
            format_func=lambda page: page['title'])

        st.sidebar.header("About the app")
        st.sidebar.write("""
        Ứng dụng dự đoán nguy cơ sinh viên tốt nghiệp quá hạn được sử dụng để dự đoán    \\
        khả năng tốt nghiệp dựa trên các tiêu chí học thuật và nhân khẩu học của sinh viên Học viện Ngân hàng.  
        """)

        st.sidebar.markdown('---')
        # st.sidebar.info("### Made by:   Nguyễn Trường Sơn")
        # st.sidebar.markdown("### [Source code](https://github.com/sonnguyen129/Predict-Student-Results)")
        # run the app function 
        page['function']()