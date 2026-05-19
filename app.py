"""
Kernexus Core - Prediction API
الملف الرئيسي لخدمة التوقع. هذا هو "المطبخ" الذي ينفذ المنطق.
"""
import pandas as pd
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# ---------- 1. إعداد التطبيق وتحميل النموذج ----------
app = FastAPI(
    title="Kernexus Core Prediction Engine",
    description="API للتنبؤ بمغادرة العملاء (Churn Prediction)",
    version="1.0.0"
)

# تحميل النموذج مرة واحدة عند بدء التشغيل
try:
    model = joblib.load('model.joblib')
    print("✅ Model loaded successfully.")
except FileNotFoundError:
    print("❌ ERROR: model.joblib not found.")
    model = None

# ---------- 2. تعريف هيكل البيانات (Pydantic Models) ----------
# هذا الهيكل يضمن أن البيانات القادمة من الواجهة صحيحة وآمنة
class CustomerData(BaseModel):
    CreditScore: int
    Geography: str
    Gender: str
    Age: int
    Tenure: int
    Balance: float
    NumOfProducts: int
    HasCrCard: int
    IsActiveMember: int
    EstimatedSalary: float

# ---------- 3. نقطة النهاية (Endpoint) ----------
@app.post("/predict")
async def predict(data: CustomerData):
    """
    نقطة النهاية الرئيسية للتوقع.
    تستقبل بيانات عميل وتعيد التوقع مع نسبة الثقة.
    """
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded")

    # تحويل البيانات المدخلة إلى DataFrame (كما يفعل Streamlit تمامًا)
    input_df = pd.DataFrame([{
        'CreditScore': data.CreditScore,
        'Geography': data.Geography,
        'Gender': data.Gender,
        'Age': data.Age,
        'Tenure': data.Tenure,
        'Balance': data.Balance,
        'NumOfProducts': data.NumOfProducts,
        'HasCrCard': data.HasCrCard,
        'IsActiveMember': data.IsActiveMember,
        'EstimatedSalary': data.EstimatedSalary
    }])

    # تنفيذ التوقع
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    # تحضير الرد
    if prediction == 0:
        result = "Customer will stay"
        confidence = probability[0] * 100
    else:
        result = "Customer will churn"
        confidence = probability[1] * 100

    return {
        "prediction": int(prediction),
        "result": result,
        "confidence": round(confidence, 2)
    }

# ---------- 4. نقطة نهاية للتحقق من الصحة ----------
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Kernexus Core Engine is running"}