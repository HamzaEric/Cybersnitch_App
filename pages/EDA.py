import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path


st.set_page_config(layout="wide")
st.title('Exploratory Data Analysis(EDA)')
st.markdown('---')
col1, col2 = st.columns([1, 2])
with col1:
    st.image('pandas.jpeg', width=500)
    st.image('datavisual.jpeg', width=500)
with col2:
    st.markdown("**Data Analysis**")
    st.write('Pandas Library')
    st.markdown('---')
    st.markdown('---')
    st.markdown("**Data Visualization**")
    st.write("1.Matplotlib")
    st.write("2.Seaborn")
st.markdown('---')
st.write('''
Welcome to the EDA section
We dive into the dataset to uncover patterns, spot anomalies, and understand the key features that distinguish phishing websites from legitimate ones.
Visualizations and descriptive statistics are used to guide our feature selection and modeling strategy, ensuring our
machine learning models are built on solid insights.
''')
st.markdown('---')

html_file=Path(r'Phishing_website_Detection_EDA.html')
components.html(html_file.read_text(), height=1000, scrolling=True)



