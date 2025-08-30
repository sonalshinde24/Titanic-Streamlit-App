# 🚢 Titanic Survival Prediction App  

This project predicts the survival of passengers on the Titanic using **Machine Learning**. The trained model is deployed as an interactive **Streamlit web app** where users can input passenger details and get survival predictions.  

🔗 **Live App:** [Click Here to Try](https://titanic-app-app-wkxtxjreesmrxeezn8ue4s.streamlit.app/)  
📂 **GitHub Repo:** [Click Here](https://github.com/sonalshinde24/titanic-app)  

---

## 📂 Project Structure  

├── .gitignore # Ignore unnecessary files (env, cache, etc.)
├── app.py # Streamlit app code
├── requirements.txt # Project dependencies
├── titanic_model.pkl # Trained ML model (Pickle file)
├── train_model.ipynb # Notebook used for training the model
└── README.md # Project documentation


---

## ⚙️ Tech Stack  

- **Python 3.x**  
- **Pandas, NumPy** – Data preprocessing  
- **Scikit-Learn** – Machine Learning model  
- **Streamlit** – Web app deployment  
- **Pickle** – Model saving/loading  

---

## 🚀 How to Run Locally  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/sonalshinde24/titanic-app.git
   cd titanic-app
   
2.**Create virtual environment (optional but recommended)**
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows

3. **Install dependencies**
pip install -r requirements.txt

4. **Run the Streamlit app**
streamlit run app.py
