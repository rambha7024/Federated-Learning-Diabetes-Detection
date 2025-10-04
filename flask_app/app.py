from flask import Flask, render_template, request
import torch
import torch.nn as nn
import numpy as np
import joblib

# ---------------- Config ----------------
MODEL_PATH = r"D:\Major Project\client_1_final_model (1).pth"   # update path if needed
SCALER_PATH = r"D:\Major Project\client_1_scaler.pkl"
N_FEATURES = 8   # Pima dataset has 8 features

# ---------------- Model ----------------
class LogisticRegression(nn.Module):
    def __init__(self, input_dim):   # ✅ fixed __init__
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))

# Load trained model
model = LogisticRegression(N_FEATURES)
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

# Load scaler
scaler = joblib.load(SCALER_PATH)

# ---------------- Flask App ----------------
app = Flask(__name__)   # ✅ fixed __name__

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Collect input values from form
        features = [
            float(request.form["pregnancies"]),
            float(request.form["glucose"]),
            float(request.form["blood_pressure"]),
            float(request.form["skin_thickness"]),
            float(request.form["insulin"]),
            float(request.form["bmi"]),
            float(request.form["dpf"]),
            float(request.form["age"]),
        ]
        
        # Scale and convert to tensor
        input_scaled = scaler.transform([features])
        input_tensor = torch.tensor(input_scaled, dtype=torch.float32)

        # Predict
        with torch.no_grad():
            output = model(input_tensor)
            prediction = 1 if output.item() > 0.5 else 0
            prob = output.item()

        result = "⚠ Diabetic" if prediction == 1 else "✅ Not Diabetic"
        css_class = "diabetic" if prediction == 1 else "non-diabetic"

        return render_template(
            "result.html", 
            prediction_text=result, 
            probability=f"{prob:.2f}",
            css_class=css_class
        )

    except Exception as e:
        return render_template(
            "result.html", 
            prediction_text=f"Error: {str(e)}", 
            probability="N/A", 
            css_class="error"
        )

if __name__ == "__main__":   # ✅ fixed __main__
    app.run(debug=True)
