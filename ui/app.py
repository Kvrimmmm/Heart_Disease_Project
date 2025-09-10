import gradio as gr
import joblib
import pandas as pd
import numpy as np

proc_csv = "data/processed/heart_processed.csv"
model_path = "models/final_model.pkl"

df = pd.read_csv(proc_csv)
feature_cols = [c for c in df.columns if c != 'target']

model = joblib.load(model_path)

def predict_raw(*args):
    x = np.array(args).reshape(1, -1)
    pred = model.predict(x)[0]
    prob = model.predict_proba(x)[0].tolist() if hasattr(model, "predict_proba") else []
    return {"prediction": int(pred), "probabilities": prob}

inputs = []
for col in feature_cols:
    inputs.append(gr.Number(label=col, value=float(df[col].median())))

outputs = [gr.Label(num_top_classes=2, label="Prediction"), gr.JSON(label="Probabilities")]

iface = gr.Interface(fn=predict_raw, inputs=inputs, outputs=outputs, title="Heart Disease Prediction (Gradio)")
iface.launch(server_name='0.0.0.0')
