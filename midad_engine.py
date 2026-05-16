import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# تحديد المسار المطلق بوضوح تام
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'midad_knowledge.db')
DATABASE_URL = f"sqlite:///{db_path}"

print(f"📡 [System] Database will be created at: {db_path}")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class MidadInsight(Base):
    __tablename__ = "midad_insights"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    category = Column(String(100))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def init_midad():
    Base.metadata.drop_all(bind=engine) # مسح أي جداول قديمة إن وجدت
    Base.metadata.create_all(bind=engine)
    print("✅ [Midad Engine] Database and Tables created successfully!")

if __name__ == "__main__":
    init_midad()