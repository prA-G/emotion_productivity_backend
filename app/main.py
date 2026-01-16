from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, auth, logic
from fastapi.security import OAuth2PasswordRequestForm

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- AUTH APIs ----------

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed = auth.hash_password(user.password)
    new_user = models.User(email=user.email, password=hashed)
    db.add(new_user)
    db.commit()
    return {"message": "User created"}

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = db.query(models.User).filter_by(email=form_data.username).first()

    if not db_user or not auth.verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = auth.create_token(db_user.id)
    return {
        "access_token": token,
        "token_type": "bearer"
    }
# ---------- PROTECTED APIs ----------

@app.post("/mood")
def log_mood(
    mood: schemas.MoodCreate,
    user_id: int = Depends(auth.get_current_user_id),
    db: Session = Depends(get_db)
):
    entry = models.MoodLog(mood=mood.mood, user_id=user_id)
    db.add(entry)
    db.commit()
    return {"message": "Mood logged"}

@app.post("/task")
def add_task(
    task: schemas.TaskCreate,
    user_id: int = Depends(auth.get_current_user_id),
    db: Session = Depends(get_db)
):
    t = models.Task(
        title=task.title,
        effort=task.effort,
        priority=task.priority,
        user_id=user_id
    )
    db.add(t)
    db.commit()
    return {"message": "Task added"}

@app.get("/tasks")
def get_tasks(
    user_id: int = Depends(auth.get_current_user_id),
    db: Session = Depends(get_db)
):
    tasks = (
        db.query(models.Task)
        .filter(models.Task.user_id == user_id)
        .all()
    )

    return {
        "tasks": [
            {
                "title": t.title,
                "effort": t.effort,
                "priority": t.priority
            }
            for t in tasks
        ]
    }

@app.get("/daily-plan")
def daily_plan(
    user_id: int = Depends(auth.get_current_user_id),
    db: Session = Depends(get_db)
):
    mood = (
        db.query(models.MoodLog)
        .filter(models.MoodLog.user_id == user_id)
        .order_by(models.MoodLog.id.desc())
        .first()
    )

    tasks = (
        db.query(models.Task)
        .filter(models.Task.user_id == user_id)
        .all()
    )

    if not mood:
        return {"tasks": []}

    plan = logic.generate_daily_plan(mood.mood, tasks)
    return {"tasks": [t.title for t in plan]}
