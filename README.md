🚢 Titanic Survival Prediction App

This project predicts the survival of passengers on the Titanic using Machine Learning. 
The trained model is deployed as an interactive Streamlit web app where users can input passenger details and get survival predictions.

🔗 Live App: Click Here to Try

📂 Project Structure
├── .gitignore              # Ignore unnecessary files (env, cache, etc.)
├── app.py                  # Streamlit app code
├── requirements.txt        # Project dependencies
├── titanic_model.pkl       # Trained ML model (Pickle file)
├── train_model.ipynb       # Notebook used for training the model
└── README.md               # Project documentation

⚙️ Tech Stack

Python 3.x
Pandas, NumPy – Data preprocessing
Scikit-Learn – Machine Learning model
Streamlit – Web app deployment
Pickle – Model saving/loading

🚀 How to Run Locally
Clone the repository

git clone https://github.com/yourusername/titanic-app.git
cd titanic-app


Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows


Install dependencies
pip install -r requirements.txt
Run the Streamlit app
streamlit run app.py

📊 Model Training
Dataset: Titanic - Machine Learning from Disaster (Kaggle)
Features used: Passenger class, age, sex, siblings/spouses, parents/children, fare, etc.
Model: Logistic Regression (you can update if you used RandomForest, DecisionTree, etc.)
Evaluation: Achieved good accuracy on test data.

🎯 Features of the App

✅ User-friendly Streamlit interface
✅ Takes passenger details as input
✅ Predicts survival chances instantly
✅ Deployed online via Streamlit Cloud
