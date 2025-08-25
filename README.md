# Insurance Charges Prediction App

A simple and interactive **web application** to predict insurance charges based on user details using a trained machine learning model.

---

## 🔹 Features

- Predict insurance charges using the following inputs:
  - Age
  - BMI
  - Number of children
  - Gender
  - Smoker status
- Interactive web interface built with **Streamlit**
- Real-time prediction without the need for a scaler (model trained on raw features)

---

## 🔹 Installation

1. **Clone the repository:**
```bash
git clone <your-repo-link>
cd <repo-folder>

2. **Install dependencies:**
pip install -r requirements.txt

3. **Required packages include:**
 Predict insurance charges using the following inputs:
  - streamlit
  - numpy
  - scikit-learn
  - pickle (built-in)

----
🔹 Usage

Run the Streamlit app:

streamlit run app.py


Enter the user details in the input fields:

Age

BMI

Number of children

Gender

Smoker status

Click Predict Charges to get the estimated insurance charges.

🔹 Model

Trained using a Linear Regression model (or specify if Lasso/KNN)

Features used:

age, bmi, children, Gender_Male, Smoker_Yes

Saved as trained_model.sav using pickle.

🔹 Notes

The model expects inputs in the same order as used during training:
age, bmi, children, Gender_Male, Smoker_Yes

No scaling is required for this model.

🔹 Screenshot (Optional)

Add a screenshot of the app here if available

🔹 License

This project is open-source and free to use for educational purposes.



