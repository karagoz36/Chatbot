# 🤖 Chatbot - FastAPI - React - Mistral AI

This project is a **Mistral AI-powered chatbot application**, developed using **FastAPI** for the backend, **React** for the frontend, and **Nginx reverse proxy** for routing.

## 📌 Features
- 🚀 **FastAPI** for a fast and scalable backend
- ⚛️ **React** for a modern and dynamic frontend
- 🐳 **Docker Compose** for orchestration
- 🔀 **Nginx Reverse Proxy**
- 🤖 **Mistral AI API** integration for an intelligent chatbot

---

## 📂 Project Structure
```
Chatbot
│── backend
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── mistral_service.py
│── frontend
│   ├── Dockerfile
│   ├── vite.config.js
│   ├── eslint.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   ├── package.json
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── index.css
│   │   ├── services/
│   │   │   ├── api.js
│── nginx
│   ├── nginx.conf
│── docker-compose.yml
│── .env
│── README.md
```

---

## 🛠️ Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/username/Chatbot.git
cd Chatbot
```

### 2️⃣ Create `.env` File and Add Mistral API Key
```bash
touch .env
```
**Contents of `.env`:**
```env
MISTRAL_API_KEY=your-mistral-api-key
```

### 3️⃣ Run Docker Containers
```bash
docker-compose up --build
```

---

## 🚀 Usage

| **Service**     | **URL**                  |
|---------------|-------------------------|
| 🌐 **Frontend** | [`http://localhost`](http://localhost) |
| 🔧 **Backend**  | [`http://localhost/api/`](http://localhost/api/) |
| 🤖 **Chatbot API** | [`http://localhost/api/chat/`](http://localhost/api/chat/) |

**Using the Chatbot:**  
1. **Enter your message.**  
2. **Click the "Send" button.**  
3. **The response from Mistral AI will be displayed on the screen.**

---

## 📜 API Endpoints

### 📝 **1. Root Endpoint**
**GET `/`**  
✅ **Response:**
```json
{
    "message": "FastAPI is running with Mistral AI"
}
```

### 🤖 **2. Chatbot API**
**POST `/chat/`**  
📩 **Request Body (JSON)**
```json
{
    "message": "Hello, how are you?"
}
```
✅ **Response:**
```json
{
    "choices": [
        {
            "message": {
                "content": "I'm an AI assistant. How can I help you today?"
            }
        }
    ]
}
```

---

## 🐳 Docker Commands
📌 **List Running Containers:**
```bash
docker ps
```
📌 **View Logs:**
```bash
docker-compose logs -f
```
📌 **Stop and Remove Containers:**
```bash
docker-compose down
```
