import streamlit as st


class MemoryManager:

    @staticmethod
    def initialize():
        if "messages" not in st.session_state:
            st.session_state.messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a professional AI Study Assistant. "
                        "Provide clear, accurate and helpful answers."
                    )
                }
            ]

    @staticmethod
    def add_user_message(message):
        st.session_state.messages.append(
            {
                "role": "user",
                "content": message
            }
        )

    @staticmethod
    def add_assistant_message(message):
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": message
            }
        )

    @staticmethod
    def get_messages():
        return st.session_state.messages

    @staticmethod
    def clear():
        st.session_state.messages = [
            {
                "role": "system",
                "content": (
                    "You are a professional AI Study Assistant. "
                    "Provide clear, accurate and helpful answers."
                )
            }
        ]