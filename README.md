# 🏥 Insurance Charges Prediction App

👉 [Live Demo on Streamlit](https://insurance-prediction-app--b5.streamlit.app/)

A simple and interactive **web application** to predict insurance
charges based on user details using a trained machine learning model.

------------------------------------------------------------------------

## 🔹 Features

-   Predict insurance charges using:
    -   Age
    -   BMI
    -   Number of Children
    -   Gender
    -   Smoker Status
-   Interactive UI built with **Streamlit**
-   Real-time predictions (no feature scaling required)
-   Pre-trained ML model for quick results

------------------------------------------------------------------------

## 🔹 Installation

1.  **Clone the repository**

``` bash
git clone <your-repo-link>
cd <your-repo-folder>
```

2.  **Install dependencies**

``` bash
pip install -r requirements.txt
```

3.  **Required packages include**

-   streamlit
-   numpy
-   scikit-learn
-   pickle (built-in)

------------------------------------------------------------------------

## 🔹 Usage

Run the Streamlit app:

``` bash
streamlit run app.py
```

### Steps:

1.  Enter the user details:
    -   Age
    -   BMI
    -   Number of children
    -   Gender
    -   Smoker status
2.  Click **Predict Charges**
3.  View the estimated charges instantly 🚀

------------------------------------------------------------------------

## 🔹 Model

-   Trained using: **Linear Regression** (or specify if Lasso/KNN is
    used)

-   Features:

        age, bmi, children, Gender_Male, Smoker_Yes

-   Model saved as: `trained_model.sav` using **pickle**

-   No scaling required (trained on raw features)

------------------------------------------------------------------------

## 🔹 Notes

-   Ensure input format matches the training order:

        age, bmi, children, Gender_Male, Smoker_Yes

-   Can be extended with more models and features.

------------------------------------------------------------------------

## 🔹 Screenshot 

<img width="999" height="720" alt="image" src="https://github.com/user-attachments/assets/66807500-7276-4c4c-81ba-4b4558f72dc2" />


------------------------------------------------------------------------

## 🔹 License

📜 This project is open-source and free to use for **educational
purposes**.
