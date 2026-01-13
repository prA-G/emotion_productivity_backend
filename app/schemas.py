from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class MoodCreate(BaseModel):
    mood: str

class TaskCreate(BaseModel):
    title: str
    effort: str
