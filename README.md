# ❤️ Heart Disease Prediction

A machine learning web application that predicts the likelihood of heart disease based on various health metrics and patient characteristics. This project uses a Logistic Regression model trained on the Heart Disease dataset.

![Heart Disease Prediction App Screenshot](screenshots/app_screenshot.png)

## 📋 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Details](#model-details)
- [Web Interface](#web-interface) 
- [License](#license)

## ✨ Features

- Predicts heart disease likelihood using medical parameters
- Clean, responsive web interface for making predictions
- Pre-trained machine learning model with good accuracy
- Detailed results with risk factor analysis
- API endpoint for integration with other applications

## 🎬 Demo

### Prediction Interface
![Prediction Interface](screenshots/prediction_interface.png)

### Results Screen
![Results Screen](screenshots/results_screen.png)

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

### 1. Train the model (optional, pre-trained model included)
```bash
python train_model.py
```

### 2. Run the web application
```bash
python app.py
```

### 3. Access the web interface
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

## 📂 Project Structure

```
heart-disease-prediction/
│
├── app.py                 # Flask web application
├── train_model.py         # Script to train the model
├── heart_model.pkl        # Trained logistic regression model
├── scaler.pkl             # StandardScaler for feature normalization
├── label_encoders.pkl     # Label encoders for categorical variables
│
├── static/
│   ├── css/
│
├── templates/
│   ├── index.html         # Main prediction form

```

## 🔬 Model Details

The heart disease prediction model is built using the following components:

- **Algorithm**: Logistic Regression
- **Features Used**:
  - Age: Patient's age in years
  - Sex: Gender (M/F)
  - ChestPainType: Type of chest pain
  - RestingBP: Resting blood pressure (mm Hg)
  - Cholesterol: Serum cholesterol (mg/dl)
  - FastingBS: Fasting blood sugar
  - RestingECG: Resting electrocardiogram results
  - MaxHR: Maximum heart rate achieved
  - ExerciseAngina: Exercise-induced angina
  - Oldpeak: ST depression induced by exercise relative to rest
  - ST_Slope: Slope of the peak exercise ST segment
- **Preprocessing**: 
  - Categorical encoding using LabelEncoder
  - Feature scaling using StandardScaler
- **Performance**:
  - Accuracy: ~85% (on test set)
  - Detailed metrics available in the classification report

## 🖥️ Web Interface

The web application provides an intuitive interface for users to:

1. Enter patient health parameters
2. Receive a heart disease prediction result
3. View risk factors and recommendations

### Input Form Fields
- Personal information (Age, Sex)
- Clinical measurements (Blood Pressure, Cholesterol, etc.)
- ECG and Exercise test results

### Results Display
- Prediction outcome (Likelihood of heart disease)
- Confidence score
- Key contributing factors
- General heart health recommendations



## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

### 📌 Note
This application is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

