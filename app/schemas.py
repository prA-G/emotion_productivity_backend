from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class MoodCreate(BaseModel):
    mood: str

class TaskCreate(BaseModel):
    title: str
    effort: str      # light / heavy
    priority: str    # low / medium / high

class TaskResponse(BaseModel):
    title: str
    effort: str
    priority: str

    class Config:
        orm_mode = True
