

# 🏦 Bank Customer Churn Prediction

This project uses machine learning to predict whether a customer will leave a U.S. bank (i.e., churn) based on their personal and financial information.

## 📊 Dataset

**Source**: [Kaggle - Bank Customer Churn Prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction/data)

**Description**:  
The dataset contains customer data from a U.S. bank and includes the following features:

- `CustomerId`, `Surname`, `RowNumber`: Identifiers (can be dropped)
- `CreditScore`: Credit score of the customer
- `Geography`: Country of residence
- `Gender`: Gender of the customer
- `Age`: Age of the customer
- `Tenure`: Number of years the customer has stayed with the bank
- `Balance`: Account balance
- `NumOfProducts`: Number of products held by the customer
- `HasCrCard`: Whether the customer has a credit card
- `IsActiveMember`: Whether the customer is an active member
- `EstimatedSalary`: Estimated salary
- `Exited`: **Target variable** — 1 if the customer left the bank, 0 otherwise

---

## 🎯 Objective

To build a classification model that predicts whether a customer will **churn (exit)** based on their attributes.

---

## 🧰 Tools & Libraries

- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- (Optional) XGBoost / LightGBM for advanced modeling

---

## 🧪 Workflow

1. **Data Preprocessing**
   - Dropping irrelevant features (`CustomerId`, `Surname`, `RowNumber`)
   - Encoding categorical variables (`Gender`, `Geography`)
   - Handling missing values (if any)
   - Feature scaling

2. **Exploratory Data Analysis (EDA)**
   - Understanding distributions
   - Correlation analysis
   - Churn rate per feature

3. **Model Building**
   - Train-test split
   - Try various models: Logistic Regression, Random Forest, XGBoost, etc.
   - Hyperparameter tuning (GridSearchCV / RandomizedSearchCV)

4. **Model Evaluation**
   - Accuracy, Precision, Recall, F1 Score
   - Confusion Matrix
   - ROC-AUC Curve

5. **Model Deployment** (Optional)
   - Flask API or Streamlit dashboard

---

## 📈 Performance Metrics

The model will be evaluated on:

- **Accuracy**: Overall performance
- **Precision/Recall**: Important for understanding false positives/negatives

---

