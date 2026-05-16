import streamlit as st
import pandas as pd
import plotly.express as px
from midad_engine import SessionLocal, MidadInsight

# 1. إعدادات الصفحة
st.set_page_config(page_title="SIMAS | Kernexus Hub", layout="wide")
st.markdown("<h1 style='text-align: left; color: #1E3A8A;'>SIMAS Control Center</h1>", unsafe_allow_html=True)
# 2. دالة تحليل الوكلاء (تأكد من وجودها في الأعلى)
def run_agent_analysis(title):
    return {
        "SIMAS": f"Strategic Roadmap: Aligning '{title}' with Riyadh tech initiatives.",
        "Distiller": "Pattern Found: Correlated with AI Localization trends.",
        "Automator": "Recommended Stack: FastAPI + Vector DB."
    }

# 3. الشريط الجانبي
with st.sidebar:
    st.header(" Agents Control")
    st.success("SIMAS: Online")
    st.info("Distiller: Active")
    st.divider()
    st.header("➕ New Insight")
    with st.form("entry_form", clear_on_submit=True):
        t = st.text_input("Insight Title")
        c = st.selectbox("Category", ["Strategic", "Technical", "Research"])
        d = st.text_area("Details")
        if st.form_submit_button("Process with Agents") and t and d:
            db = SessionLocal()
            new = MidadInsight(title=t, category=c, content=d)
            db.add(new); db.commit(); db.close()
            st.rerun()

# 4. العرض الرئيسي
#st.title("          SIMAS Control Center")
st.subheader("")

db = SessionLocal()
items = db.query(MidadInsight).all()
db.close()

if items:
    df = pd.DataFrame([{"Title": i.title, "Category": i.category} for i in items])
    
    # تعريف res هنا بناءً على آخر سجل لضمان عدم وجود NameError
    res = run_agent_analysis(items[-1].title)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.write("### 📊 Distribution")
        fig = px.pie(df, names='Category', hole=0.4)
        fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=300)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.write("### Multi-Agent Analysis")
        with st.expander(" SIMAS (Strategic Intelligence Agent)", expanded=True):
            st.info(res["SIMAS"])
        with st.expander("🔍 Distiller (Knowledge Engine)"):
            st.warning(res["Distiller"])
        with st.expander("⚙️ Automator (Solution Architect)"):
            st.success(res["Automator"])
    
    st.divider()
    st.write("### 📂 Complete Repository")
    st.dataframe(df, use_container_width=True)
else:
    st.info("System Ready. Waiting for data input to activate agents...")