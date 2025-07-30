# Telecom Customer Churn Prediction App

A machine learning-powered web application that predicts whether a telecom customer is likely to churn (leave the company) or stay, based on customer demographics, contract details, and service usage patterns.

---

## Table of Contents

- [Overview](#overview)
- [Business Problem](#business-problem)
- [Approach and Solution](#approach-and-solution)
- [Algorithms Used](#algorithms-used)
- [Model Performance](#model-performance)
- [Features](#features)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**Telecom Churn Prediction App** is designed to help telecom operators identify customers at risk of leaving, enabling targeted retention strategies and improved customer satisfaction.

---

## Business Problem

Customer churn significantly affects the telecom industry's revenue. Retaining customers is far more cost-effective than acquiring new ones. Predictive analytics helps businesses make data-driven decisions to minimize churn and implement timely retention efforts.

---

## Approach and Solution

- **Data Preprocessing:** Includes handling missing data, encoding categorical features, and scaling.
- **Feature Engineering:** Identification and selection of the most relevant features for churn prediction.
- **Model Training:** Multiple machine learning algorithms were evaluated to predict churn.
- **Deployment:** The best model is served via a user-friendly web interface for real-time predictions.

---

## Algorithms Used

- **Logistic Regression**
- **Decision Tree**
- **Random Forest**
- **Gradient Boosting**
- **Support Vector Machine**
- **Ensemble Methods**

(Random Forest and ensemble models often provide the best performance for this task.)

---

## Model Performance

- **Accuracy:** Typically ranges from 78% to 90% depending on algorithm and dataset.
- **Key Metrics:** Accuracy, Precision, Recall, F1-score, Confusion Matrix.
- *Note:* Maximizing recall for the churn class is emphasized, as flagging actual churners is most valuable.

---

## Features

- Simple web UI to input customer information
- Instant prediction of churn probability
- Actionable output for business decision-making

---

## Setup & Installation

1. **Clone this repository:**
    ```
    git clone https://github.com/mrsaurabhtanwer/Telecom-Customer-Churn-Prediction-App.git
    cd Telecom-Customer-Churn-Prediction-App
    ```

2. **Set up the virtual environment:**
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```
    streamlit run app.py
    ```

---

## Usage

1. Open the web app (usually runs at `http://localhost:8501`).
2. Enter customer details as prompted.
3. Receive churn prediction (“Will Churn” / “Will Not Churn”) with probability.

---

## Results

Example:

- Input: Customer contract type, tenure, payment methods, monthly charges, etc.
- Output:  
    ```
    Probability of Churn: 78%
    Prediction: Likely to Churn
    ```
- Enables targeted retention actions.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request or open an issue for feedback.

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or collaboration, please contact [Your Name] or create an issue on GitHub.

# Telecom-Customer-Churn-Prediction-App
[App](https://telecom-customer-churn-prediction-app-mrsaurabhtanwer.streamlit.app/)
