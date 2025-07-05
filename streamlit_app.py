import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import io

# Load saved model and scaler
model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("📉 Telecom Customer Churn Prediction App")
st.markdown("Enter customer information below to predict if they are likely to churn.")

# Input fields for user
with st.form("churn_form"):
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Has Partner", [0, 1])
    dep = st.selectbox("Has Dependents", [0, 1])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 500.0)
    contract = st.selectbox("Contract", ['Month-to-month', 'One year', 'Two year'])
    payment = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    internet = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])
    submitted = st.form_submit_button("Predict")

# Full feature list from training (example, replace with your actual list)
required_features = [
    'SeniorCitizen',
    'tenure',
    'MonthlyCharges',
    'TotalCharges',
    'gender_Male',
    'Partner_Yes',
    'Dependents_Yes',
    'PhoneService_Yes',
    'MultipleLines_No phone service',
    'MultipleLines_Yes',
    'InternetService_Fiber optic',
    'InternetService_No',
    'OnlineSecurity_No internet service',
    'OnlineSecurity_Yes',
    'OnlineBackup_No internet service',
    'OnlineBackup_Yes',
    'DeviceProtection_No internet service',
    'DeviceProtection_Yes',
    'TechSupport_No internet service',
    'TechSupport_Yes',
    'StreamingTV_No internet service',
    'StreamingTV_Yes',
    'StreamingMovies_No internet service',
    'StreamingMovies_Yes',
    'Contract_One year',
    'Contract_Two year',
    'PaperlessBilling_Yes',
    'PaymentMethod_Credit card (automatic)',
    'PaymentMethod_Electronic check',
    'PaymentMethod_Mailed check'
]

# Build data dict with all features, set 0 for those not in UI
data = {feature: 0 for feature in required_features}
# Set values from UI
data['SeniorCitizen'] = senior
data['tenure'] = tenure
data['MonthlyCharges'] = monthly
data['TotalCharges'] = total
data['gender_Male'] = 1 if gender == "Male" else 0
data['Partner_Yes'] = partner
data['Dependents_Yes'] = dep
data['Contract_One year'] = 1 if contract == 'One year' else 0
data['Contract_Two year'] = 1 if contract == 'Two year' else 0
data['PaymentMethod_Credit card (automatic)'] = 1 if payment == 'Credit card (automatic)' else 0
data['PaymentMethod_Electronic check'] = 1 if payment == 'Electronic check' else 0
data['PaymentMethod_Mailed check'] = 1 if payment == 'Mailed check' else 0
data['InternetService_Fiber optic'] = 1 if internet == 'Fiber optic' else 0
data['InternetService_No'] = 1 if internet == 'No' else 0
# ...add more mappings if you add more UI fields...

input_df = pd.DataFrame([data])
input_df = input_df[required_features]

# Scale input
scaled_input = scaler.transform(input_df)

# Prediction + Visualization
if submitted:
    prediction = model.predict(scaled_input)
    prob = model.predict_proba(scaled_input)[0][1]

    st.subheader("🔍 Prediction Result")
    if prediction[0] == 1:
        st.error(f"⚠️ This customer is likely to churn. (Confidence: {prob*100:.2f}%)")
    else:
        st.success(f"✅ This customer is likely to stay. (Confidence: {(1-prob)*100:.2f}%)")

    # Show pie chart
    fig, ax = plt.subplots()
    ax.pie([1 - prob, prob], labels=['Not Churn', 'Churn'], autopct='%1.1f%%', colors=['#28a745', '#dc3545'])
    ax.set_title("Churn Probability")
    st.pyplot(fig)

    # Show user input summary
    st.subheader("📋 Input Summary")
    st.write(input_df)

    # Add download prediction option
    download_df = input_df.copy()
    download_df['Churn Prediction'] = ['Yes' if prediction[0] == 1 else 'No']
    csv = download_df.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Download Prediction", data=csv, file_name='churn_prediction.csv', mime='text/csv')

# Reset button (fake reset via rerun)
if st.button("🔄 Reset Form"):
    st.rerun()
