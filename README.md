# 🤖 AI Study Assistant

An AI-powered Study Assistant built using **Python**, **Streamlit**, and **Groq API**.

The application allows users to:

- 💬 Chat with an AI assistant
- 📊 Upload Excel datasets
- 📈 View dataset statistics
- 🤖 Ask AI questions about uploaded datasets
- 💾 Export chat history

---

## Features

- AI Chat using Groq API
- Conversation Memory
- Excel Dataset Upload
- Dataset Preview
- Missing Value Detection
- Statistical Summary
- AI Dataset Analysis
- Download Chat History

---

## Technologies Used

- Python
- Streamlit
- Groq API
- Pandas
- OpenPyXL
- Python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/AI_STUDY_ASSISTANT.git
```

Go to project folder:

```bash
cd AI_STUDY_ASSISTANT
```

Install requirements:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
MODEL_NAME=llama-3.1-8b-instant
```

Run the app:

```bash
streamlit run app.py
```

---

## Screenshots

### Home Page

![Home](assets/home_page.png)

---

### Upload Dataset

![Dataset](assets/dataset_upload.png)

---

### AI Answer

![Answer](assets/ai_dataset_answer.png)

---

### Download Chat

![Download](assets/chat_download.png)

---

## Project Structure

```
AI_STUDY_ASSISTANT/
│
├── assets/
├── config/
├── data/
├── services/
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## Author

Sundas Abrar