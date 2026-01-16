# 🌱 Emotional State–Aware Productivity Backend

A human-centric backend system that generates daily task plans by considering a user’s **emotional state, task effort, and task priority**, helping users stay productive without burnout.

---

## 💡 Why This Project?

Most productivity tools assume users can perform at the same intensity every day.  
This project introduces **emotion-aware decision-making**, allowing productivity to adapt to mental energy and urgency.

---

## 🚀 Key Features

- 🔐 JWT-based authentication (signup & login)
- 👤 User-specific data isolation
- 🧠 Emotion-aware task filtering
- ⚖️ Priority-aware logic for urgent tasks
- 📋 View all tasks with effort & priority
- 📊 Dynamic daily plan generation

---

## 🛠️ Tech Stack

- Python  
- FastAPI  
- SQLite  
- SQLAlchemy ORM  
- OAuth2 + JWT  
- Passlib (bcrypt)  
- Swagger UI  

---

## 🔄 How It Works

1. User signs up and logs in (JWT issued)
2. User logs emotional state:
   - `low`, `overwhelmed`, `neutral`, `energized`
3. User adds tasks with:
   - effort: `light` / `heavy`
   - priority: `low` / `medium` / `high`
4. Backend generates daily plan using rule-based logic:
   - Light tasks are always included
   - Heavy tasks require sufficient energy
   - **High-priority tasks appear even on low-energy days**

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|------|---------|-------------|
| POST | `/signup` | Create user |
| POST | `/login` | Login & get JWT |
| POST | `/mood` | Log emotional state |
| POST | `/task` | Add task |
| GET  | `/tasks` | View all user tasks |
| GET  | `/daily-plan` | Get emotion-aware task plan |

All endpoints are **JWT-protected**.

---

## ▶️ Run the Project

```bash
venv\Scripts\activate
python -m uvicorn app.main:app --reload
```

---

## 🌍 Why This Matters

This backend can power:

- Mental health & wellness applications  
- Smart planners & habit trackers  
- Corporate productivity tools  
- Burnout-prevention systems  
- Emotion-aware AI assistants  

It demonstrates **human-centered backend system design**, not just CRUD APIs.

---

## 🔮 Future Enhancements

- Task completion & deadlines  
- Mood analytics & insights  
- AI-based task recommendations  
- Frontend / mobile integration  
- Database migrations with Alembic  

---

## 👩‍💻 Author

**Pragati Dwivedi**  
Aspiring Backend Engineer | Python Developer
