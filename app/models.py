from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

class MoodLog(Base):
    __tablename__ = "mood_logs"

    id = Column(Integer, primary_key=True)
    mood = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    effort = Column(String)  # light / heavy
    user_id = Column(Integer, ForeignKey("users.id"))
