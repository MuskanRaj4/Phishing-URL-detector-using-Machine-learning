# Phishing URL Detector

## 📌 Project Overview
Phishing URL Detector is a Machine Learning-based web application that identifies whether a URL is **Safe** or **Phishing**. The application uses a trained classification model and provides predictions through a simple Flask web interface.

## 🎯 Objective
The objective of this project is to improve cybersecurity awareness by detecting potentially malicious URLs using machine learning techniques.

## 🚀 Features
- Detects Safe and Phishing URLs
- User-friendly Flask web interface
- Machine Learning prediction model
- Fast and accurate URL classification
- Easy to use and lightweight

## 🛠️ Technologies Used
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS
- Joblib

## 📂 Project Structure
Phishing-URL-Detector/
│── app.py
│── train.model.py
│── phishing_model.pkl
│── phishing_url_dataset.csv
│── templates/
│     └── index.html
│── static/
│     └── style.css
│── README.md


## ⚙️ Installation

1. Clone the repository
git clone https://github.com/your-username/Phishing-URL-Detector.git


2. Install dependencies
pip install flask pandas numpy scikit-learn joblib

3. Train the model (Optional)
python train.model.py


4. Run the application
python app.py

5. Open your browser
http://127.0.0.1:5000

## 📊 Model Performance
- Machine Learning Algorithm: Random Forest Classifier
- Model Accuracy: **91.56%**

## 📸 Output
The application accepts URL-related features as input and predicts whether the URL is:

- ✅ Safe URL
- ⚠️ Phishing URL

## 🔮 Future Improvements
- Direct URL input instead of manual feature entry
- Real-time phishing detection
- Domain reputation checking
- Browser extension integration
- Deep Learning-based detection

## 👩‍💻 Author
MUSKAN RAJ

## 📜 License
This project is created for educational and learning purposes.