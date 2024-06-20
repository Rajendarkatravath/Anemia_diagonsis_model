import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the dataset with a spinner
data = pd.read_csv("E:/data_science_projects/Anemia_diagonis_model/diagnosed_cbc_data_v4.csv")

# Create a sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # required
        options=["Statistics", "Plots"],  # required
        icons=["house", "bar-chart"],  # optional
        menu_icon="cast",  # optional
        default_index=0,  # optional
    )

# Define the pages
if selected == "statistics":
    st.title("Welcome to statistics Page")

    # disribing the stats of the data

if st.button("dataset statistics"):
    stats=data.describe()

    st.write(stats)

    

elif selected == "Plots":
    st.title("Welcome to Plots Page")

    # Display different plots
    fig_hist = px.histogram(data, x='WBC', title='Histogram of WBC')
    st.plotly_chart(fig_hist)

    fig_scatter = px.scatter(data, x='WBC', y='LYMp', title='Scatter Plot of WBC vs LYMp')
    st.plotly_chart(fig_scatter)

    fig_line = px.line(data, x='WBC', y='LYMp', title='Line Chart of WBC vs LYMp')
    st.plotly_chart(fig_line)

    fig_box = px.box(data, x='WBC', title='Box Plot of WBC')
    st.plotly_chart(fig_box)

    fig_combined = make_subplots(rows=2, cols=2, subplot_titles=('Histogram', 'Scatter Plot', 'Line Chart', 'Box Plot'))
    fig_combined.add_trace(go.Histogram(x=data['WBC']), row=1, col=1)
    fig_combined.add_trace(go.Scatter(x=data['WBC'], y=data['LYMp'], mode='markers'), row=1, col=2)
    fig_combined.add_trace(go.Scatter(x=data['WBC'], y=data['LYMp'], mode='lines'), row=2, col=1)
    fig_combined.add_trace(go.Box(y=data['WBC']), row=2, col=2)
    fig_combined.update_layout(height=800, width=800, title_text="Combined Plots")
    st.plotly_chart(fig_combined)
