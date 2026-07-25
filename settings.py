import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Groq Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")

# Dataset Path
DATASET_PATH = "data/Dataset for Data Analytics.xlsx"

# App Configuration
APP_TITLE = "AI Study Assistant"
APP_ICON = "🤖"

# Chat Settings
MAX_HISTORY = 20
TEMPERATURE = 0.7