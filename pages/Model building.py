import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(layout="wide")
st.title('Machine Learning Model Building')
st.markdown('---')
col1, col2 = st.columns([1, 2])
with col1:
    st.image('TensorFlow.jpeg', width=500)
    st.image('sklearn.jpeg', width=600)
with col2:

    st.markdown("**Best Performing Ensemble Model**")
    st.write('XGBoost(Extreme Gradient Boosting Model)')
    st.markdown('---')
    st.markdown('---')
    st.markdown("**Best Performing Deep Learning Model**")
    st.markdown("MultiLayer Perceptron(MLP) Neural Network")

st.markdown('---')
st.write('''
MLP and XGBoost emerged as the top-performing models in our phishing website detection Model Building, delivering the highest accuracy and overall performance
compared to other algorithms evaluated.
''')
st.markdown('---')

html_file = Path('Model_Building_in_Phising_Website_Detection.html')
components.html(html_file.read_text(encoding='utf-8', errors='replace'), height=1000, scrolling=True)

