# Federated-Learning-Diabetes-Detection
Federated Learning-Based Privacy-Preserving Diabetes Detection with Encrypted Computation
# Federated Learning - Privacy-Preserving Diabetes Detection

📌 **Final Year Project**  
🔬 **Author:** Rambha Rasmitha Lekha

---

## 📖 Abstract
This project proposes a **privacy-preserving federated learning framework** for diabetes detection.  
- Local models are trained at each client (hospital/medical center) using **Logistic Regression**.  
- Model updates are encrypted using **Homomorphic Encryption (CKKS)** before aggregation.  
- The global model is built securely without exposing raw patient data or intermediate updates.  

Our approach ensures **data confidentiality** while achieving strong predictive performance on medical datasets.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x  
- **Libraries:** PyTorch, TenSEAL, NumPy, Pandas, scikit-learn  
- **Concepts:** Federated Learning, Homomorphic Encryption (CKKS), Logistic Regression  

---

## 📊 Dataset
- **Pima Indians Diabetes Dataset** (UCI ML Repository)  
  - 768 samples  
  - Features: pregnancies, glucose, blood pressure, BMI, etc.  
  - Target: Diabetes diagnosis (1 = yes, 0 = no)  

---

## 📈 Results
- **Accuracy:** ~82%  
- **Precision:** ~76%  
- **Recall:** ~69%  
- **F1-Score:** ~72.5%  
- **AUC:** 0.86  

These results show stable performance across multiple clients in a federated learning setup.

---

## 📂 Repository Contents
- `Project_Report.docx` → Full project documentation  
- `README.md` → Project summary (this file)  
- *(Future)* `src/` → Source code for training and evaluation  
- *(Future)* `results/` → Graphs and output plots  

---

## 🚀 Future Work
- Extend framework to **deep learning models**.  
- Add **differential privacy** to strengthen protection.  
- Deploy as a web app for real-time predictions.  

---

## 📜 License
MIT License  

---

## 📧 Contact
If you found this useful or want to collaborate:  
**Rambha**  
rambhasrasmi7024@gmail.com  

