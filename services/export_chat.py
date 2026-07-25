import json
import streamlit as st


class ChatExporter:

    @staticmethod
    def download(messages):

        chat = json.dumps(
            messages,
            indent=4
        )

        st.download_button(
            label="📥 Download Chat History",
            data=chat,
            file_name="chat_history.json",
            mime="application/json"
        )