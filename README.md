# 🩺 Federated Learning - Privacy-Preserving Diabetes Detection

📌 **Final Year Project**  
👩‍💻 **Author:** Rambha Rasmitha Lekha

---

## 📖 Abstract
This project implements a **privacy-preserving federated learning framework** for diabetes detection.  

- Each client trains a local **Logistic Regression model** on its dataset.  
- Model updates are encrypted with **Homomorphic Encryption (CKKS)** before aggregation.  
- A global model is built securely, without exposing raw patient data or gradients.  

Our approach ensures **data confidentiality** while achieving high predictive performance on medical datasets.

---

## 🛠️ Tech Stack
- **Languages:** Python, Flask (for web app)  
- **Libraries:** PyTorch, TenSEAL, NumPy, Pandas, scikit-learn, Joblib  
- **Concepts:** Federated Learning (FL), Homomorphic Encryption (HE), Logistic Regression  

---

## 📊 Dataset
- **Pima Indians Diabetes Dataset** (UCI ML Repository)  
  - 768 samples  
  - 8 numerical features (glucose, BMI, insulin, etc.)  
  - Binary target: Diabetic (1) / Not Diabetic (0)  

---

## 📈 Results
- **Accuracy:** ~82%  
- **Precision:** ~76%  
- **Recall:** ~69%  
- **F1-Score:** ~72.5%  
- **AUC:** 0.86  

These results show **stable and reliable performance** across multiple clients in a federated setting.

---

## 🖥️ Flask Web Application
A simple Flask app is provided in the `flask_app/` folder to test the diabetes prediction model via a web interface.  

### 🔹 Run the app locally:
```bash
cd flask_app
pip install -r requirements.txt
python app.py
