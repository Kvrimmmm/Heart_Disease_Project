import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/processed/heart_processed.csv")
X = df.drop(columns=['target'])
y = df['target']

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
joblib.dump(clf, "models/final_model.pkl")
print("model saved to models/final_model.pkl")
