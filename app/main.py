from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, auth, logic

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    new_user = models.User(email=user.email, password=hashed)
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@app.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter_by(email=user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token(db_user.id)
    return {"access_token": token}

@app.post("/mood")
def log_mood(mood: schemas.MoodCreate, db: Session = Depends(get_db)):
    entry = models.MoodLog(mood=mood.mood, user_id=1)
    db.add(entry)
    db.commit()
    return {"message": "Mood logged"}

@app.post("/task")
def add_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    t = models.Task(title=task.title, effort=task.effort, user_id=1)
    db.add(t)
    db.commit()
    return {"message": "Task added"}

@app.get("/daily-plan")
def daily_plan(db: Session = Depends(get_db)):
    mood = db.query(models.MoodLog).order_by(models.MoodLog.id.desc()).first()
    tasks = db.query(models.Task).all()
    plan = logic.generate_daily_plan(mood.mood, tasks)
    return {"tasks": [t.title for t in plan]}
