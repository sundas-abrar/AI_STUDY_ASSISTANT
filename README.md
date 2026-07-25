# 🤖 AI Study Assistant

A professional AI Study Assistant built using **Python**, **Streamlit**, **Groq LLM**, and **Pandas**. This application allows users to chat with an AI assistant, upload Excel datasets, analyze data, and maintain conversation memory during the session.

---

## 📌 Features

- 🤖 AI Chatbot using Groq LLM
- 🧠 Conversation Memory
- 📊 Upload Excel (.xlsx) Datasets
- 📋 Dataset Preview
- 📈 Dataset Statistics
- ❓ Missing Value Analysis
- 💬 AI-powered Dataset Question Answering
- 📥 Download Chat History
- 🏗️ Modular Python Architecture

---

## 🛠 Technologies Used

- Python 3
- Streamlit
- Groq API
- Pandas
- OpenPyXL
- Python Dotenv

---

## 📂 Project Structure

```
AI_STUDY_ASSISTANT/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── config/
│   └── settings.py
│
├── services/
│   ├── llm.py
│   ├── memory.py
│   ├── dataset_loader.py
│   ├── data_assistant.py
│   └── export_chat.py
│
├── data/
└── assets/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add your API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

### Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

Add screenshots of:

- Home Screen
- Dataset Upload
- Dataset Preview
- AI Chat
- Dataset Analysis

inside the `assets/` folder.
## Home Page

![Home](assets/home_page.png)

## Upload Dataset

![Upload](assets/dataset_upload.png)

## AI Answer

![Answer](assets/ai_dataset_answer.png)

## Download Chat

![Download](assets/chat_download.png)
---

## 👩‍💻 Author

**Sundas Abrar**

Bachelor of Science in Computer Science
