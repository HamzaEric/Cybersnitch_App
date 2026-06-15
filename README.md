# CyberSnitch: Phishing Website Detection Platform

CyberSnitch is a full-stack, machine learning-powered security application designed to detect and analyze phishing URLs in real-time. By leveraging parallelized gradient boosting and deep multi-layer neural networks, the platform evaluates domain characteristics, URL structures, and security indicators to classify websites as legitimate or malicious. 

Deployed seamlessly via Streamlit Cloud, CyberSnitch acts as an intelligent first line of defense against social engineering and credential harvesting vectors.

---

##  Key Features

- **Dual-Model Cognitive Engine:** Utilizes optimized **XGBoost** and **Multi-Layer Perceptron (MLP)** architectures for consensus-based threat classification.
- **Real-Time URL Parsing:** Extracts structural, lexical, and security features (e.g., HTTPS status, subdomain depth, anchor URL consistency) instantly upon submission.
- **Robust Exception Handling:** Graceful handling of network timeouts, invalid inputs, and edge cases to ensure consistent application uptime.

---

##  Machine Learning Architecture

The detection engine parses incoming URLs into structured feature sets, processing them through two distinct mathematical approaches to minimize false positives:

### 1. Multi-Layer Perceptron (MLP) Classifier
A feedforward artificial neural network (ANN) trained to discover complex non-linear combinations across URL vectors.
- **Layers:** Multi-layered dense network architecture.
- **Activation Function:** ReLU / Logistic optimization.
- **Optimizer:** Adam (Adaptive Moment Estimation) for precise weight adjustments across highly sparse categorical boundaries.

### 2. XGBoost (Extreme Gradient Boosting)
An optimized distributed gradient boosting library implementing regularized tree boosting (`gbtree`).
- **Objective:** Binary classification (`binary:logistic`).
- **Strengths:** Exceptional handling of structured tabular data, robust feature importance ranking, and built-in L1/L2 regularization to prevent overfitting on specific domain high-frequency terms.

---

##  Tech Stack

- **Core Language:** Python 3.11+
- **Frontend / Deployment:** Streamlit (UI Engine), Streamlit Cloud
- **Data Engineering:** Pandas, NumPy
- **Machine Learning & Modeling:** Scikit-Learn, XGBoost, Joblib / Pickle
- **Environment & Package Management:** Ubuntu (Linux Environment OS), `uv` / `pip`

---
