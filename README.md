# Kernexus Core - Prediction API

<div dir="rtl">

## 🧠 محرك التوقع المركزي لنظام Kernexus

خدمة API مبنية باستخدام FastAPI للتنبؤ بمغادرة العملاء (Customer Churn Prediction). هذا هو "المطبخ" الخلفي الذي ينفذ عمليات التعلم الآلي ويقدم النتائج عبر RESTful API.

## 🚀 الميزات الرئيسية
- **تنبؤ عالي الدقة**: يستخدم نموذج تعلم آلة مدرب مسبقًا.
- **توثيق تلقائي**: واجهة Swagger UI تفاعلية على `/docs`.
- **هيكل احترافي**: مبني بمبدأ فصل الاهتمامات (Separation of Concerns).
- **جاهز للنشر**: يمكن رفعه على أي خادم يدعم Python.

## 🛠️ التقنيات المستخدمة
- Python 3.10+
- FastAPI
- Scikit-learn / Pandas / NumPy
- Uvicorn
- Pydantic

## 📋 المتطلبات الأساسية
- Python 3.10 أو أحدث
- pip

## ⚙️ طريقة التشغيل المحلي

1. **انسخ المستودع:**
   ```bash
   git clone https://github.com/your-username/kernexus-core.git
   cd kernexus-core