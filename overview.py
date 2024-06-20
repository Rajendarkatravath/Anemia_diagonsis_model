import streamlit as st
import base64

def app():
    st.title("Data Analysis Dashboard")
    st.header("Overview")
    st.markdown("""
    Welcome to the **Anemia Diagnosis Analysis and Model Development App**!

    This dashboard is designed to help you analyze and visualize your data with ease. Below, you'll find an overview of the main features and instructions on how to use the dashboard.

    ## Key Features
  
    - **Data Visualization:** Create interactive plots to explore your data.
    - **Statistical Analysis:** Perform basic statistical analyses like mean, median, and standard deviation.
    - **Machine Learning:** Build and evaluate machine learning models directly from your browser.

   
    ## Contact
    If you have any questions or feedback, feel free to reach out at [your-email@example.com](mailto:your-email@example.com).

    We hope you find this dashboard useful for your data analysis needs!
    """)

if __name__ == "__main__":
    app()
