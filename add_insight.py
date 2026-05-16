from midad_engine import SessionLocal, MidadInsight

def save_to_midad(title, category, content):
    db = SessionLocal()
    try:
        new_entry = MidadInsight(
            title=title,
            category=category,
            content=content
        )
        db.add(new_entry)
        db.commit()
        print(f"🚀 [Midad] Recorded: {title}")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # تسجيل أول تدوينة تقنية تعكس رؤيتك لـ Kernexus
    save_to_midad(
        title="AI Localization in Riyadh",
        category="Strategic",
        content="Developing proprietary AI agents to automate Saudi business workflows."
    )