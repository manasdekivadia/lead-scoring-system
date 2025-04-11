# 🧠 Lead Scoring System

A full-stack AI-powered web application that helps businesses evaluate and prioritize leads. Built with **FastAPI** (Python) for the backend and **React** for the frontend. The system uses a pre-trained ML model (`model.pkl`) to assign scores to leads based on custom logic.

## 🚀 Features

- 🔥 **FastAPI Backend** — blazing fast, async Python API
- ⚛️ **React Frontend** — clean, responsive UI
- 🤖 **ML-Driven Scoring** — score leads via a trained `model.pkl`
- 🌐 **RESTful Architecture** — seamless data flow between front and back
- ☁️ **Deploy-Ready** — `render.yaml` config for cloud deployment (Render.com or similar)

---

## 📁 Project Structure

```bash
lead-scoring-system/
│
├── backend/                # FastAPI backend
│   ├── main.py             # Main FastAPI application
│   ├── model.pkl           # Trained ML model for scoring
│   ├── requirements.txt    # Python dependencies
│   ├── render.yaml         # Deployment config for Render
│   ├── package.json        # (optional) for frontend preview if needed
│
├── frontend/               # React frontend
│   ├── src/                # React components & logic
│   ├── public/             # Static files
│   ├── package.json        # Node dependencies
│
├── .gitignore
└── README.md               # You're here!
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/manasdekivadia/lead-scoring-system.git
cd lead-scoring-system
```

---

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

➡️ FastAPI will run at: `http://127.0.0.1:8000`

#### Optional:
To explore the API docs:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

---

### 3. Frontend Setup (React)

```bash
cd ../frontend
npm install
npm start
```

➡️ React app runs at: `http://localhost:3000`

---

## 🌍 Deployment

You can deploy this project using [Render](https://render.com) or any platform that supports FastAPI + React apps.

- The `backend/render.yaml` file is preconfigured for deployment.
- You can host the frontend separately (e.g., Netlify, Vercel) or configure full-stack hosting.

---

## 🧪 Sample ML Model

The `model.pkl` file is a serialized machine learning model that scores leads based on your predefined logic. Make sure the input format to the model matches what it was trained on.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---
