# 🍷 Wine Quality Predictor

Welcome to the **Wine Quality Predictor**! This project uses **machine learning** to predict the quality of wine based on various chemical properties.

## 🚀 Live Demo
[Click here to access the deployed app](https://wine-quality-predictor.streamlit.app)

## 📌 Features
- Predicts wine quality on a scale of **0-8**
- Takes **chemical composition** as input (e.g., acidity, alcohol, pH, etc.)
- Supports **Red & White wine classification**
- **User-friendly Streamlit UI**
- **Deployed on Streamlit Cloud**

## 🏗 Tech Stack
- **Python** (Pandas, NumPy, Scikit-Learn, XGBoost)
- **Streamlit** (for interactive UI)
- **GitHub** (version control & deployment)

## 📂 Project Structure
```
📁 wine-quality-predictor
│── 📄 app.py                # Streamlit app
│── 📄 requirements.txt      # Dependencies
│── 📄 winequalityN.csv      # Dataset
│── 📄 xgb_wine_quality.pkl  # Trained Model
│── 📄 scaler.pkl            # Data Scaler
│── 📄 README.md             # Project Documentation
```

## 🔧 Installation & Usage
### 1️⃣ Clone the repository
```sh
git clone https://github.com/shital8580/wine-quality-predictor.git
cd wine-quality-predictor
```
### 2️⃣ Install dependencies
```sh
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit app
```sh
streamlit run app.py
```

## 📊 Dataset Details
The dataset contains various chemical attributes of **red & white wines** along with quality ratings.
### Key Features:
- **Fixed Acidity**
- **Volatile Acidity**
- **Citric Acid**
- **Residual Sugar**
- **Chlorides**
- **Free Sulfur Dioxide**
- **Total Sulfur Dioxide**
- **Density**
- **pH**
- **Sulphates**
- **Alcohol**
- **Wine Type (Red/White)**
- **Quality Score (0-8)**

## 📌 Model Training
- **Algorithm:** XGBoost Classifier
- **Preprocessing:** Standard Scaler
- **Label Encoding:** Wine Type & Quality
- **Accuracy:** ~85%
# Wine Quality Categories
Quality	Category	Description
0-4	🚫 Very Poor- Not present in your dataset

5	⚠️ Poor- Acceptable but lacks complexity & balance

6	👍 Average- Decent quality, moderate flavor & balance

7	✅ Good	- Well-balanced, enjoyable taste

8	⭐ Best-	High-quality wine with great taste & aroma

## 📤 Deployment
The model is deployed using **Streamlit Cloud**.
### Steps to Deploy:
1. Push changes to GitHub.
2. Connect the repo with **Streamlit Cloud**.
3. Streamlit automatically deploys the latest version.

## 👨‍💻 Author
- **Shital Chavan**  
🚀 _Passionate about AI & ML projects!_

