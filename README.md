# 🚀 Project Budget Prediction App
### *Machine Learning + Streamlit Deployment*

This project is an end-to-end machine learning application that predicts the **estimated budget for a software project** based on multiple engineering, management, and technical parameters. The model is deployed using **Streamlit**, making it simple and interactive for users to input project details and instantly generate a cost estimate.

---

## 📌 Project Overview
Accurately predicting the project budget is a major challenge for organizations due to varying factors such as team size, complexity, stakeholder involvement, and schedule pressure.  
This ML-based solution helps overcome the guesswork by offering **data-driven budget estimation**.

The project includes:
- Data preprocessing & exploration  
- Machine learning model building  
- Model evaluation & optimization  
- Deployment using Streamlit  
- Real-time prediction with a trained Random Forest model (`reg.pkl`)

---

## 🔍 Problem Statement
Software project estimation is often inaccurate due to subjective judgment. Factors affecting budget include:

- Team size  
- Timeline  
- Complexity  
- Stakeholder involvement  
- Technology familiarity  
- Integration & dependency complexity  

Traditional estimation methods lack consistency and reproducibility.

---

## 🎯 Objective
To build a machine learning model that predicts the **estimated project budget** using key software engineering parameters and deploy it as a **Streamlit app**.

---

## 🛠 Tech Stack
| Component | Tools |
|----------|-------|
| **Frontend / Deployment** | Streamlit |
| **Data Handling** | pandas, numpy |
| **Modeling** | scikit-learn |
| **Model Used** | Random Forest Regressor |
| **Environment** | Python |
| **Packaging** | Pickle (`reg.pkl`), requirements.txt |

---

## ⚙️ Methodology

### 1️⃣ Data Preprocessing & Feature Engineering
Performed inside the Jupyter Notebook:
- Cleaned dataset  
- Converted categorical fields  
- Outlier handling  
- Train/test split  
- Feature selection  

### 2️⃣ Model Training
Tested multiple algorithms:
- Linear Regression  
- Decision Tree  
- Random Forest Regressor (*selected for best accuracy*)

The final model was saved as **reg.pkl**.

### 3️⃣ Deployment Using Streamlit
The Streamlit UI (`7 Deployment.py`) provides:
- Number inputs  
- Radio buttons  
- Real-time prediction  
- Clean UI with emojis  

---

## 🧠 Model Input Features

| Feature | Description |
|--------|-------------|
| Team_Size | Total members assigned |
| Estimated_Timeline_Months | Duration of the project |
| Complexity_Score | Technical difficulty level |
| Stakeholder_Count | Number of stakeholders |
| External_Dependencies_Count | Number of integrations |
| Change_Request_Frequency | Frequency of requirement changes |
| Technology_Familiarity | New / Familiar / Expert |
| Schedule_Pressure | Time constraint |
| Integration_Complexity | System integration difficulty |

---

## 📁 Project Structure

```
Project-Budget-Prediction/
│── merged_project_budget_data.csv   #data in csv format 
│── ml budget final project.ipynb     # Training Notebook
│── Deployment.py                    # Streamlit App
│── reg.pkl                            # Trained Model
│── requirements.txt                   # Dependencies
│── README.md                          # Documentation
```

---

## ▶ How to Run the Project Locally

### 1️⃣ Clone the Repository
```
git clone https://github.com/SaiPraneethMarripelli/Project-Budget-Prediction.git
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App
```
streamlit run "Deployment.py"
```

### 4️⃣ Use the Application
Enter project details → click **Submit for Prediction** → view estimated budget.

---

## 📈 Key Outcomes
- Fully interactive Streamlit UI  
- Accurate predictions with Random Forest  
- End-to-end ML pipeline: data → model → deployment  
- Real-time budget estimation  

---

## 🚀 Future Improvements
- Add project risk scoring  
- Deploy to cloud (Streamlit Cloud / AWS / Azure)  
- Build REST API using FastAPI  
- Add visualization dashboard  
- Include confidence intervals for predictions  

---

## 👤 Author
**Sai Praneeth Marripelli**  
📧 Email: saipraneethmarripelli@gmail.com  
🔗 LinkedIn: www.linkedin.com/in/saipraneeth-marripelli-2003sai

---

## ⭐ Support  
If you found this project helpful, give it a **⭐ on GitHub**!
