from groq import Groq

from config.settings import (
    GROQ_API_KEY,
    GROQ_MODEL,
    TEMPERATURE
)


class LLMService:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_response(self, messages, dataset_context=""):

        try:

            if dataset_context:

                system_message = {
                    "role": "system",
                    "content": f"""
You are an AI Study Assistant.

Use the uploaded dataset whenever the user asks questions about the uploaded data.

Dataset Information:

{dataset_context}
"""
                }

                final_messages = [system_message] + messages

            else:
                final_messages = messages

            completion = self.client.chat.completions.create(
                model=GROQ_MODEL,
                temperature=TEMPERATURE,
                messages=final_messages
            )

            return completion.choices[0].message.content

        except Exception as e:
            return (
    "⚠️ Sorry, something went wrong while "
    "contacting the AI model.\n\n"
    f"Details:\n{e}"
)