# Kuch Plan Hai? 🎯  
**AI-Based Activity Planner Based on Mood, Budget, and Location**  

Kuch Plan Hai? is a smart activity planning app that helps users decide what to do based on their **mood**, **budget**, and **location**. It uses AI to generate personalized activity suggestions across categories like food, entertainment, shopping, wellness, and more.  

The app integrates **FastAPI + PostgreSQL** on the backend and **React** on the frontend, with clean modular code and scalable design.  

---

## 🚀 Features  

- **AI Assistant Chatbox** – Conversational planning with AI.  
- **Activity Categories** – 8 core categories:  
  1. 🍽️ Food  
  2. 🎭 Entertainment  
  3. 🧗 Activities  
  4. 🏙️ Causal Hangouts
- **Smart Filters** – Plan by travel distance (Nearby, Within City, Explore More).  
- **User System** – Login, save plans, track preferences.  
- **Social Sharing** – Share plans via WhatsApp.  

---

## 🛠️ Tech Stack  

### Backend (FastAPI + PostgreSQL)  
- FastAPI – REST API framework  
- PostgreSQL – Relational database  
- SQLAlchemy – ORM  
- Pydantic – Data validation  
- JWT Authentication (planned)  

### Frontend (React)  
- React + Vite – Modern frontend  
- TailwindCSS – Styling  

---

## 📂 Project Structure  

```
kuch-plan-hai/
│── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── routes/
│   │   ├── controllers/
│   │   ├── db.py
│   │   └── config.py
│   ├── schema.sql
│   └── requirements.txt
│
│── frontend/
│   ├── package.json
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── services/
│   └── public/
│
└── README.md
```

---

## ⚡ Getting Started  

### Backend Setup  
```bash
cd backend
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup  
```bash
cd frontend
npm install
npm run dev
```

---

## 📌 Roadmap  
- 🔲 Healthcheck endpoint (backend)  
- 🔲 React frontend setup  
- 🔲 User authentication  
- 🔲 Activity categories API  
- 🔲 AI-powered suggestions  
- 🔲 Social sharing & filters  
- 🔲 Deployment  

---


