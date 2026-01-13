# 🌱 Emotional State–Aware Productivity Backend

> **A human-centric backend system that adapts daily task planning based on a user’s emotional state — because productivity should respect humans, not exhaust them.**

---

## 🧠 Why This Project Exists

In today’s tech-driven world, people are expected to be productive every day at the same intensity, regardless of how they feel.

But humans are not machines.

- Some days we feel energized
- Some days we feel overwhelmed
- Some days we are mentally exhausted

Most productivity systems completely ignore emotional state.

This project was built to answer one core question:

> **What if software adapted to human emotions instead of forcing humans to adapt to software?**

---

## 🚀 What This Project Does

This backend system dynamically generates a **daily task plan** based on a user’s **current emotional state**.

### Core Concept
- Users log how they feel (mood)
- Users add tasks with effort levels
- The backend intelligently filters tasks based on mood
- On low-energy days → only light tasks are suggested
- On high-energy days → all tasks are allowed

The goal is to support **sustainable productivity**, not burnout-driven output.

---

## 🛠️ Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy (ORM)
- JWT Authentication
- Passlib + bcrypt (password hashing)
- Swagger UI (API testing)

---

## 📂 Project Structure
emotion_productivity_backend/
│
├── app/
│ ├── main.py # API routes
│ ├── database.py # Database configuration
│ ├── models.py # Database models
│ ├── schemas.py # Request & response schemas
│ ├── auth.py # Authentication & password hashing
│ ├── logic.py # Emotion-based business logic
│
├── run_server.bat # One-click server launcher (Windows)
├── app.db # SQLite database (ignored in Git)
├── requirements.txt
└── README.md

---

## 🔄 How the System Works

### 1️⃣ User Authentication
- Users can sign up and log in securely
- Passwords are hashed using bcrypt
- JWT tokens are issued on login

### 2️⃣ Mood Logging
Users log their current emotional state:
- `low`
- `overwhelmed`
- `neutral`
- `energized`

### 3️⃣ Task Creation
Tasks are created with effort levels:
- `light`
- `heavy`

### 4️⃣ Daily Plan Generation
The backend applies rule-based logic:

- If mood is `low` or `overwhelmed`  
  → only light tasks are returned
- If mood is `neutral` or `energized`  
  → all tasks are returned

All decision-making logic resides in the backend.

---

## 🧪 Running the Project (Windows)

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies from `requirements.txt`
4. Double-click the file:
- `run_server.bat`
5. Swagger UI will open automatically at:
  http://127.0.0.1:8000/docs
  

---

## 🌍 Why This Project Is Important

### 💻 Tech Professionals
- Helps prevent burnout
- Encourages sustainable work patterns
- Respects mental energy levels

### 🎓 Students
- Supports flexible study planning
- Reduces guilt on low-energy days

### 🏢 Corporate Productivity Tools
- Can be integrated into internal task systems
- Supports employee wellness initiatives

### 📱 Mental Health & Wellness Applications
- Backend logic can power habit trackers and focus apps
- Can support emotion-aware digital tools

### 🤖 Intelligent Systems & AI Assistants
- Can be extended with analytics and recommendations
- Useful for adaptive systems and smart planners

---

## 🔮 Future Enhancements

- JWT-protected user-specific task isolation
- Mood history tracking and analytics
- AI-based mood prediction
- Mobile application integration
- Burnout risk indicators
- Team productivity insights

---

## 💡 Design Philosophy

> **Productivity should be compassionate.**  
> **Software should understand humans.**  
> **Technology should reduce pressure, not increase it.**

---

## 👩‍💻 Author

**Pragati Dwivedi**  
Aspiring Backend Engineer | Python Developer

---

## ⭐ Final Note

This project is not just a CRUD backend.  
It demonstrates:
- Backend architecture fundamentals
- Clean API design
- Business logic separation
- Human-centered system thinking

Built with empathy and real-world relevance.


