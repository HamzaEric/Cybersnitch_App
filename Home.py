import streamlit as st
import pickle
import numpy as np
import streamlit.components.v1 as components
from pathlib import Path
import re
import warnings
warnings.filterwarnings('ignore')
import time

 st.set_page_config(layout='wide')

def normalize_url(url):
    # Lowercase and strip 'www.' from the domain part
    url = url.lower()
    if url.startswith("http://") or url.startswith("https://"):
        scheme, rest = url.split("://", 1)
        if rest.startswith("www."):
            rest = rest[4:]
        url = scheme + "://" + rest
    return url

# Feature extraction function
def extract_features(url):
    # Use_of_HTTP check first
    use_of_http = 0 if url.startswith("https://") else 1

    # Normalize URL
    url = url.strip().lower().replace("https://", "").replace("http://", "")

    features = []

    # URL Length
    features.append(len(url))

    # having_At_Symbol
    features.append(1 if "@" in url else 0)

    # Prefix_Suffix
    domain = url.split("//")[-1].split("/")[0]
    features.append(1 if "-" in domain else 0)

    # Use_of_HTTP
    features.append(0 if url.startswith("https://") else 1)

    # TinyURL
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.ly|cutt\.ly|rb\.gy"
    features.append(1 if re.search(shortening_services, url) else 0)

    # URL_Depth
    depth = url.split("//")[-1].count("/")
    features.append(min(depth,4))

    # Redirection
    features.append(1 if url.count("//") > 1 else 0)

    return features



   
    st.title('CyberSnitch')
    st.markdown('---')

    col1,col2 = st.columns([1, 2])
    with col1:
        st.image('cybersnitch.jpeg', width=600)
    with col2:
        st.markdown(" A Web app designed to detect phishing websites using machine learning techniques </h3 >", unsafe_allow_html=True)
        st.markdown('---')
        st.markdown(" 1. Multilayer Perceptron ")
        st.markdown(" 2. XGBoost Classifier ")

    st.markdown('---')
    st.code('Its a combination of two fields i.e. Cybersecurity and Data Science aiming to protect users from cyber threats using machine learning')
    st.markdown('---')
    st.header('Introduction')
    st.markdown('---')
    st.write('''
     This project focuses on phishing website detection, leveraging machine learning techniques to identify malicious websites based on various features and behavioral patterns.
    The system analyzes elements such as URL structure and domain age to distinguish phishing sites from legitimate ones.
    By training the model on a labeled dataset of phishing and legitimate websites, the project aims to build a predictive model that can accurately classify unknown sites in real-time.
    ''')
    st.markdown('---')
    st.header('A User-Centric Approach And Retraining For User-friendliness')
    st.markdown('---')

    st.write('''
     This app has been carefully designed with user-friendliness in mind.
     Whether you're a regular user or someone with web development experience, the interface
     is intuitive and requires only a simple URL input — no complex forms, no external API requirements.
    ''')
    st.write('## How user-friendliness is implemented')
    st.info('''
    ### The App is designed with simplicity as you cannot tell a user who has no knowledge of websites to input whether the website has an Iframe,DNS record,right-click disabled to hide page source,Mouse Over Method,Webtraffic Or Domain_Age
    ''')
    html_file = Path('Retraining_For_UI.html')
    components.html(html_file.read_text(encoding='utf-8', errors='replace'), height=1000, scrolling=True)

    st.markdown('---')

    with st.sidebar:
        st.caption("CyberSnitch URL Scanner Status")
        st.success("✅ Operational")

    # Model selection
    selected_model = st.radio("## Choose a Machine Learning Model", ["XGBoostClassifier(Supervised Machine Learning Model)", "MLPClassifier(Deep Learning Model)"])
    if selected_model=='XGBoostClassifier(Supervised Machine Learning Model)':
     st.success('XGBoost Model Loaded successfully')
    else:
     st.success('MLP Model Loaded successfully')

    # Load models
    with open('MLPClassifier.pickle.dat', 'rb') as file:
        mlp_model = pickle.load(file)

    with open('XGBoostClassifier.pickle.dat', 'rb') as file:
        xgb_model = pickle.load(file)

    # User input
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image('urlscanner.jpeg', width=600)
    with col2:
        st.markdown(
            "<h3 style='font-size: 70px;margin-top:15px;'> CyberSnitch URL Scanner </h3 >",
            unsafe_allow_html=True)

        st.code('A Digital Watchdog against phishing threats')

    url_input = st.text_input("Enter the website URL:")
    if st.button("Detect"):
        if not url_input:
            st.warning("Please enter a URL.")
        else:
            with st.spinner("Analyzing URL features..."):
             time.sleep(1)  # Simulate processing

            if url_input.startswith("http://"):
                prediction = 1  # Force as phishing
                explanation = "The URL starts with 'http://' which is a common trait in phishing websites and if legit it is not secure since its not encrypted"
            else:
                # Extract features and run through the model
                normalized_url = normalize_url(url_input)
                input_features = np.array(extract_features(normalized_url)).reshape(1, -1)

                model = xgb_model if selected_model == "XGBoost" else mlp_model
                prediction = int(model.predict(input_features)[0])
                explanation = "Prediction based on machine learning model analysis of the URL's structure."

            result = "🔒 Legitimate" if prediction == 0 else "⚠️ Phishing"
            st.subheader(f"Prediction: {result}")
            st.info(f"Reason: {explanation}")
            if prediction == 0:
                st.info(
                    "✅ This website appears to be **legitimate** based on the analyzed features. You can proceed safely, but always stay alert online.")
                st.info('''
                     This website is classified as safe due to the absence of phishing indicators such as the use of IP addresses, abnormal URL length, excessive special characters, misleading subdomains, or redirection patterns.
                     The overall feature profile aligns with typical characteristics of legitimate websites.
                ''')
            else:
                st.warning(
                    "⚠️ This website shows signs of **phishing** behavior. Be cautious and avoid entering any personal information.")

                st.warning("⚠️ If you are sure this is a phishing website you can add it to the cybersecurity updates on"
                           "    cybersnitch community or PhishTank to inform other users to stay safe online")



