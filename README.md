# 🎓 AI Study Assistant

An AI-powered Study Assistant built with **Streamlit**, **Groq LLM**, and **Pandas**. This application allows users to upload Excel/CSV datasets, PDF and Word documents, or images, chat with an AI assistant about them, maintain conversation history, and export chat conversations.

---

## ✨ Features

- ✨ AI-powered chatbot using Groq API (`openai/gpt-oss-120b` by default)
- 📊 Upload and analyze Excel (.xlsx) and CSV datasets
- 📖 Upload and read PDF and Word (.docx) documents
- 🖼️ Upload images (with optional OCR text extraction)
- 🧠 Conversation memory
- 📈 Dataset preview and statistics
- 🏷️ Display dataset columns
- 🕳️ Missing value analysis
- 📑 Dataset summary
- 📤 Export chat history
- 🎨 Clean, white & cream interface set in Inter, the same typeface used by GitHub, Stripe, and Notion

---

## 📁 Project Structure

```
AI_STUDY_ASSISTANT/
│
├── assets/
│   ├── ai_dataset_answer.png
│   ├── chat_download.png
│   ├── dataset_upload.png
│   └── home_page.png
│
├── .streamlit/
│   └── config.toml
│
├── config/
│   └── settings.py
│
├── services/
│   ├── data_assistant.py
│   ├── dataset_loader.py
│   ├── document_loader.py
│   ├── export_chat.py
│   ├── llm.py
│   └── memory.py
│
├── .env
├── .env.example
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## 📎 Supported File Uploads

| Type | Extensions | What happens |
|---|---|---|
| Tabular data | `.xlsx`, `.xls`, `.csv` | Loaded into pandas; preview, columns, missing values, and summary stats shown |
| Documents | `.pdf`, `.docx` | Text extracted and shown as a preview; page/word counts displayed |
| Images | `.png`, `.jpg`, `.jpeg` | Displayed inline; text extracted via OCR if the `tesseract-ocr` system package is installed |

In every case, the extracted content is passed to the AI as context, so you can ask questions about the uploaded file directly in chat.

> **Note on OCR:** `pytesseract` needs the `tesseract-ocr` binary installed on your system (e.g. `sudo apt install tesseract-ocr` on Ubuntu/Debian, or `brew install tesseract` on macOS). Without it, images still upload and display fine — just without text extraction.

---

## 🎨 Design

- **Palette:** white & cream background (`#FFFDF8` / `#F4ECD8`) with warm brown-tan accents, dark charcoal text for readability — set in `.streamlit/config.toml` and polished with extra CSS in `app.py`.
- **Typeface:** [Inter](https://fonts.google.com/specimen/Inter), loaded via Google Fonts, with a native system-font fallback (`-apple-system`, `Segoe UI`, `Roboto`) so the app still looks clean if the web font can't load.
- **Icon:** 🎓 is used as the browser tab icon and page title.

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Groq API
- Pandas
- OpenPyXL
- python-dotenv
- Tiktoken

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/sundas-abrar/AI_STUDY_ASSISTANT.git
cd AI_STUDY_ASSISTANT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📷 Application Preview

### 🏠 Home Page

![Home Page](assets/home_page.png)

---

### 📁 Upload Dataset

![Dataset Upload](assets/dataset_upload.png)

---

### 🎓 AI Answer Using Uploaded Dataset

![AI Dataset Answer](assets/ai_dataset_answer.png)

---

### 📤 Export Chat

![Chat Download](assets/chat_download.png)

---

## 📦 Requirements

```
streamlit>=1.47.0
groq>=0.31.0
pandas>=2.3.0
openpyxl>=3.1.5
python-dotenv>=1.1.1
tiktoken>=0.10.0
pypdf>=4.3.0
python-docx>=1.1.2
Pillow>=10.4.0
pytesseract>=0.3.10
```

---

## 👩‍💻 Author

**Sundas Abrar**

GitHub: https://github.com/sundas-abrar

---

## 📄 License

This project is created for educational purposes.