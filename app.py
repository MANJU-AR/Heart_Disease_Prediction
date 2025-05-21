from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load model, scaler, and encoders
model = joblib.load("heart_model.pkl")
scaler = joblib.load("scaler.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Feature names in the correct order
feature_names = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol',
                 'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina',
                 'Oldpeak', 'ST_Slope']

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    input_data = {}

    if request.method == "POST":
        try:
            # Collect inputs
            for feature in feature_names:
                input_data[feature] = request.form[feature]

            # Apply label encoding to categorical features
            input_values = []
            for feature in feature_names:
                value = input_data[feature]
                if feature in label_encoders:
                    le = label_encoders[feature]
                    value = le.transform([value])[0]
                else:
                    value = float(value)
                input_values.append(value)

            # Scale and predict
            input_array = np.array([input_values])
            input_scaled = scaler.transform(input_array)
            result = model.predict(input_scaled)[0]
            prediction = "⚠️ High Risk of Heart Attack" if result == 1 else "✅ Low Risk of Heart Attack"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction, input_data=input_data)

if __name__ == "__main__":
    app.run(debug=True)
