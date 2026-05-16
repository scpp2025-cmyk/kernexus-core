from midad_engine import SessionLocal, MidadInsight

def fetch_all_insights():
    db = SessionLocal()
    insights = db.query(MidadInsight).all()
    
    print("\n--- 🇸🇦 Midad Knowledge Repository ---")
    for item in insights:
        print(f"ID: {item.id} | Title: {item.title}")
        print(f"Category: {item.category}")
        print(f"Content: {item.content}")
        print(f"Date: {item.created_at}")
        print("-" * 40)
    db.close()

if __name__ == "__main__":
    fetch_all_insights()