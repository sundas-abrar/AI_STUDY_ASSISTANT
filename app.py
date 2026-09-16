import streamlit as st

from config.settings import APP_TITLE, APP_ICON
from services.llm import LLMService
from services.memory import MemoryManager
from services.dataset_loader import DatasetLoader
from services.document_loader import DocumentLoader
from services.data_assistant import DataAssistant
from services.export_chat import ChatExporter


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide"
)

# =====================================================
# VISUAL THEME (white / cream, dark readable text)
# =====================================================
# Base colors come from .streamlit/config.toml.
# This CSS polishes a few Streamlit elements that don't
# fully follow the theme by default, and keeps text dark
# and legible on every surface.

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
    html, body, .stApp, [class*="st-"], [class*="css"], button, input, textarea, select {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
    }

    /* Streamlit's icons (chat avatars, upload/expander/arrow icons) are
       rendered as ligature text through the Material Symbols icon font.
       The broad font override above would turn those icons back into
       literal words ("face", "smart_toy", "upload"...), so restore the
       icon font specifically for every element that renders one. */
    [data-testid="stIconMaterial"],
    [data-testid="stIconMaterial"] *,
    span[class*="material-symbols"],
    i[class*="material-symbols"] {
        font-family: 'Material Symbols Rounded' !important;
    }

    .stApp {
        background-color: #FFFDF8;
    }

    /* Main title */
    h1 {
        color: #4A3B2A !important;
        font-weight: 800;
        letter-spacing: -0.5px;
    }

    h2, h3, h4 {
        color: #4A3B2A !important;
        font-weight: 700;
        letter-spacing: -0.2px;
    }

    p, li, span, label, .stMarkdown, .stCaption {
        color: #2E2A24;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #F4ECD8;
        border-right: 1px solid #E4D8BC;
    }

    section[data-testid="stSidebar"] * {
        color: #2E2A24 !important;
    }

    /* Welcome / info banner */
    div[data-testid="stAlertContainer"] {
        background-color: #FBF3E1 !important;
        border: 1px solid #E4D8BC !important;
        border-radius: 10px;
        color: #4A3B2A !important;
    }
    div[data-testid="stAlertContainer"] * {
        color: #4A3B2A !important;
    }

    /* Chat messages */
    div[data-testid="stChatMessage"] {
        background-color: #FFFFFF;
        border: 1px solid #EFE6D2;
        border-radius: 14px;
        padding: 6px 4px;
        margin-bottom: 8px;
        box-shadow: 0 1px 3px rgba(74, 59, 42, 0.06);
    }

    /* Chat input box */
    div[data-testid="stChatInput"] {
        background-color: #FFFFFF;
        border: 1px solid #E4D8BC;
        border-radius: 12px;
    }
    div[data-testid="stChatInput"] textarea {
        color: #2E2A24 !important;
    }

    /* Buttons */
    .stButton button, .stDownloadButton button {
        background-color: #A9825C;
        color: #FFFDF8 !important;
        border: none;
        border-radius: 8px;
        font-weight: 600;
    }
    .stButton button:hover, .stDownloadButton button:hover {
        background-color: #8F6C48;
        color: #FFFDF8 !important;
    }

    /* Metrics */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #EFE6D2;
        border-radius: 10px;
        padding: 10px;
    }
    div[data-testid="stMetricValue"] {
        color: #4A3B2A !important;
    }
    div[data-testid="stMetricLabel"] {
        color: #6B5B45 !important;
    }

    /* Expanders */
    details {
        background-color: #FFFFFF;
        border: 1px solid #EFE6D2 !important;
        border-radius: 10px;
    }
    summary {
        color: #4A3B2A !important;
        font-weight: 600;
    }

    /* Dataframes / tables */
    div[data-testid="stDataFrame"] {
        border: 1px solid #EFE6D2;
        border-radius: 8px;
    }

    /* File uploader */
    section[data-testid="stFileUploaderDropzone"] {
        background-color: #FFFFFF;
        border: 1.5px dashed #C9B48B;
        border-radius: 10px;
    }

    hr {
        border-color: #E4D8BC !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎓 AI Study Assistant")

st.info("""
✨ **Welcome!**

This AI Study Assistant can:

- 📊 Analyze Excel & CSV datasets
- 📖 Read PDF and Word documents
- 🖼️ Accept image uploads
- 💬 Chat using Groq AI
- 🧠 Remember the conversation
- ⬇️ Download chat history
""")

# =====================================================
# INITIALIZE SERVICES
# =====================================================

MemoryManager.initialize()

llm = LLMService()
dataset = DatasetLoader()
document = DocumentLoader()

uploaded_file = None
dataset_context = ""

TABULAR_EXTENSIONS = (".xlsx", ".xls", ".csv")
DOCUMENT_EXTENSIONS = (".pdf", ".docx")
IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg")

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("🗂️ Upload a File")

    uploaded_file = st.file_uploader(
        "Upload a dataset, document, or image",
        type=["xlsx", "xls", "csv", "pdf", "docx", "png", "jpg", "jpeg"],
        help="Supported formats: Excel, CSV, PDF, Word (.docx), and images (PNG/JPG)."
    )

    if uploaded_file is not None:

        filename_lower = uploaded_file.name.lower()

        # -------------------------------------------------
        # Tabular data: Excel / CSV
        # -------------------------------------------------
        if filename_lower.endswith(TABULAR_EXTENSIONS):

            dataset.load_dataset(uploaded_file)

            rows, cols = dataset.get_shape()

            dataset_context = dataset.get_dataset_context()

            st.success("✅ Dataset Loaded Successfully")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Rows", rows)

            with col2:
                st.metric("Columns", cols)

            st.write(f"**File:** {uploaded_file.name}")

            with st.expander("🔍 Preview Dataset"):
                st.dataframe(dataset.get_preview())

            with st.expander("🏷️ Column Names"):
                st.write(dataset.get_columns())

            with st.expander("🕳️ Missing Values"):
                st.dataframe(dataset.get_missing_values())

            with st.expander("📈 Dataset Summary"):
                st.dataframe(dataset.get_summary())

        # -------------------------------------------------
        # Documents: PDF / Word
        # -------------------------------------------------
        elif filename_lower.endswith(DOCUMENT_EXTENSIONS):

            document.load(uploaded_file)

            dataset_context = document.get_context()

            st.success("✅ Document Loaded Successfully")

            st.write(f"**File:** {uploaded_file.name}")

            if document.kind == "pdf":
                st.write(f"**Pages:** {document.page_count}")

            st.write(f"**Word count:** {document.get_word_count()}")

            with st.expander("📝 Preview Extracted Text"):
                st.write(document.get_preview())

        # -------------------------------------------------
        # Images
        # -------------------------------------------------
        elif filename_lower.endswith(IMAGE_EXTENSIONS):

            document.load(uploaded_file)

            dataset_context = document.get_context()

            st.success("✅ Image Loaded Successfully")

            st.write(f"**File:** {uploaded_file.name}")

            st.image(document.image, use_container_width=True)

            if document.text:
                with st.expander("🔠 Extracted Text (OCR)"):
                    st.write(document.get_preview())
            elif not document.ocr_available:
                st.caption(
                    "ℹ️ OCR isn't available on this machine, so text inside "
                    "the image couldn't be read. Install the `tesseract-ocr` "
                    "system package to enable it."
                )
            else:
                st.caption("ℹ️ No text was detected in this image.")

    st.divider()

    st.header("📤 Export Chat")

    ChatExporter.download(
        MemoryManager.get_messages()
    )

    st.divider()

    st.header("🧾 About")

    st.write("""
**AI Study Assistant**

Features:

- ✨ Groq LLM
- 🧠 Conversation Memory
- 📊 Excel / CSV Dataset Analysis
- 📖 PDF & Word Document Reading
- 🖼️ Image Uploads
- 🎨 Streamlit Interface
- 🧩 Modular Python Architecture
""")

# =====================================================
# TOP BUTTONS
# =====================================================

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("🧹 Clear Chat"):
        MemoryManager.clear()
        st.rerun()

with col2:
    st.caption(
        f"💬 Messages: {len(MemoryManager.get_messages()) - 1}"
    )

# =====================================================
# CHAT HISTORY
# =====================================================

for message in MemoryManager.get_messages():

    if message["role"] == "system":
        continue

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================================================
# CHAT INPUT
# =====================================================

prompt = st.chat_input("Ask me anything about your studies or uploaded file...")

if prompt:

    MemoryManager.add_user_message(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤔 Thinking..."):

        # Try answering with Python first (only works for tabular data)
        response = DataAssistant.answer(prompt, dataset)

        # Otherwise use the AI model
        if response is None:
            response = llm.generate_response(
                MemoryManager.get_messages(),
                dataset_context
            )

    MemoryManager.add_assistant_message(response)

    with st.chat_message("assistant"):
        st.markdown(response)
