❤️ Heart Disease Prediction Project

Looking for a quick overview? Check the Short Version.

📌 **Overview**
This project is a Machine Learning application that predicts the likelihood of heart disease using the UCI Heart Disease dataset.  
It was developed as part of my AI & Machine Learning journey to practice building a full ML pipeline and deploying it with Gradio for real-time interaction.

The workflow covers everything from data preprocessing and feature engineering, to model training, evaluation, optimization, and deployment with a lightweight user interface.

🗂️ **Project Structure**


Heart_Disease_Project/
│── data/
│ └── heart_disease.csv # Dataset
│── notebooks/
│ ├── 01_data_preprocessing.ipynb # Data cleaning & preprocessing
│ ├── 02_pca_analysis.ipynb # Dimensionality Reduction (PCA)
│ ├── 03_feature_selection.ipynb # Feature selection & importance
│ ├── 04_supervised_learning.ipynb # Logistic Regression, SVM, RF, etc.
│ ├── 05_unsupervised_learning.ipynb # K-Means & Hierarchical Clustering
│ ├── 06_hyperparameter_tuning.ipynb # GridSearchCV & RandomizedSearchCV
│── models/
│ └── final_model.pkl # Exported trained model
│── ui/
│ └── app.py # Gradio web application
│── deployment/
│ └── ngrok_setup.txt # Ngrok guide for deployment
│── results/
│ └── evaluation_metrics.txt # Accuracy, precision, recall, F1, AUC
│── README.md
│── requirements.txt
│── .gitignore


🛠️ **Technologies Used**
- **Programming Language**: Python 3.9+
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **ML Workflow**: Data Preprocessing, PCA, Feature Selection, Supervised & Unsupervised Learning, Hyperparameter Tuning
- **Deployment Tools**: Gradio (UI), Ngrok (for public access), GitHub
- **Notebooks**: Jupyter Notebook

🚀 **How to Run**

1️⃣ Clone the repository
```bash
git clone https://github.com/Kvrimmmm/Heart_Disease_Project.git
cd Heart_Disease_Project


2️⃣ Install dependencies

pip install -r requirements.txt


3️⃣ Run the Gradio App

cd ui
python app.py


4️⃣ (Optional) Deploy publicly with Ngrok
Follow the steps inside deployment/ngrok_setup.txt
ذ
```
ذّ`
👨‍💻 **Author**  
Karim Khaled  

🔗 [GitHub](https://github.com/Kvrimmmm)  
🔗 [LinkedIn](https://www.linkedin.com/in/karim-khaled)  
