import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("titanic_model.pkl")

st.title("🚢 Titanic Survival Prediction")

# Input fields
pclass = st.selectbox("Class (1=First, 2=Second, 3=Third)", [1,2,3])
sex = st.selectbox("Sex", ["male","female"])
age = st.slider("Age", 1, 80, 30)
sibsp = st.number_input("Siblings/Spouses Aboard", min_value=0, max_value=10, value=0)
parch = st.number_input("Parents/Children Aboard", min_value=0, max_value=10, value=0)
fare = st.number_input("Fare", min_value=0.0, value=32.0)
embarked = st.selectbox("Port of Embarkation", ["S","C","Q"])

# Convert categorical like training
sex = 0 if sex == "female" else 1
embarked_map = {"C":0, "Q":1, "S":2}
embarked = embarked_map[embarked]

# Prepare input
input_data = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked]],
                          columns=["pclass","sex","age","sibsp","parch","fare","embarked"])

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("🎉 Survived!")
    else:
        st.error("💀 Did not survive")
