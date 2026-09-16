import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Groq Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")

# App Configuration
APP_TITLE = "AI Study Assistant"
APP_ICON = "🎓"

# Chat Settings
MAX_HISTORY = 20
TEMPERATURE = 0.7