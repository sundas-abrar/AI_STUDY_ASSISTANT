import streamlit as st

from config.settings import APP_TITLE, APP_ICON
from services.llm import LLMService
from services.memory import MemoryManager
from services.dataset_loader import DatasetLoader
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

st.title("🤖 AI Study Assistant")

st.info("""
👋 **Welcome!**

This AI Study Assistant can:

- 📊 Analyze Excel datasets
- 💬 Chat using Groq AI
- 🧠 Remember the conversation
- 📁 Display dataset statistics
- 📥 Download chat history
""")

# =====================================================
# INITIALIZE SERVICES
# =====================================================

MemoryManager.initialize()

llm = LLMService()
dataset = DatasetLoader()

uploaded_file = None
dataset_context = ""

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("📊 Dataset")

    uploaded_file = st.file_uploader(
        "Upload Excel Dataset",
        type=["xlsx"]
    )

    if uploaded_file is not None:

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

        with st.expander("📄 Preview Dataset"):
            st.dataframe(dataset.get_preview())

        with st.expander("📋 Column Names"):
            st.write(dataset.get_columns())

        with st.expander("❓ Missing Values"):
            st.dataframe(dataset.get_missing_values())

        with st.expander("📈 Dataset Summary"):
            st.dataframe(dataset.get_summary())

    st.divider()

    st.header("💾 Chat")

    ChatExporter.download(
        MemoryManager.get_messages()
    )

    st.divider()

    st.header("ℹ️ About")

    st.write("""
**AI Study Assistant**

Features:

- ✅ Groq LLM
- ✅ Conversation Memory
- ✅ Excel Dataset Analysis
- ✅ Streamlit Interface
- ✅ Modular Python Architecture
""")

# =====================================================
# TOP BUTTONS
# =====================================================

col1, col2 = st.columns([1, 4])

with col1:
    if st.button("🗑 Clear Chat"):
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

prompt = st.chat_input("Ask me anything about your studies or dataset...")

if prompt:

    MemoryManager.add_user_message(prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤔 Thinking..."):

        # Try answering with Python first
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