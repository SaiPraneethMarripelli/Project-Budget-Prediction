import streamlit as st
import pandas as pd
import pickle

# Title and Subtitle with Emojis
st.title("💰 Project Budget Estimator")
st.subheader("📝 Enter Project Details Below")

# Input Fields
Team_Size = st.number_input("👥 Team Size:", min_value=2, max_value=50, step=1)
Estimated_Timeline_Months = st.number_input("🕒 Estimated Timeline (Months):", min_value=2, max_value=36, step=1)
Complexity_Score = st.number_input("📊 Complexity Score (1.5 - 10.0):", min_value=1.50, max_value=10.00)
Stakeholder_Count = st.number_input("👨‍💼 Stakeholder Count:", min_value=2, max_value=30, step=1)
External_Dependencies_Count = st.radio("🔗 External Dependencies:", [0, 1, 2, 3, 4, 5, 6, 7])
Change_Request_Frequency = st.number_input("🔁 Change Request Frequency (0.01 - 8.84):", min_value=0.01, max_value=8.84)
Technology_Familiarity = st.radio("🧠 Technology Familiarity:", ['New', 'Familiar', 'Expert'])
Schedule_Pressure = st.number_input("⏱️ Schedule Pressure (0.00 - 0.58):", min_value=0.00, max_value=0.58)
Integration_Complexity = st.number_input("⚙️ Integration Complexity (1.0 - 10.0):", min_value=1.00, max_value=10.00)

# Load Trained Random Forest Model
with open("reg.pkl", "rb") as f:
    rfr = pickle.load(f)

# Submit Button
if st.button("🚀 Submit for Prediction"):
    input_data = [[
        Team_Size,
        Estimated_Timeline_Months,
        Complexity_Score,
        Stakeholder_Count,
        External_Dependencies_Count,
        Change_Request_Frequency,
        Technology_Familiarity,
        Schedule_Pressure,
        Integration_Complexity
    ]]
    prediction = rfr.predict(input_data)
    st.success(f"💵 Estimated Project Budget (USD): **${prediction[0]:,.2f}**")

if st.button("<< Back"):
    st.switch_page(r"pages/6 Model Building.py")

if st.button("Go to Main Page >>"):
    st.switch_page("Introduction.py")