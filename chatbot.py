from utils import OPENAI_API_KEY
from iconfig import INIT_CHAT_HISTORY
from openai import OpenAI
import streamlit as st


def preinit():
    if "history" not in st.session_state:
        st.session_state["history"] = INIT_CHAT_HISTORY.copy()

class CustomerDataChatbot:
    def __init__(self):
        preinit()
        self.openai_model = "gpt-3.5-turbo"
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.history = st.session_state["history"]

    def ask(self, prompt):
        self.history.append({"role": "user", "content": prompt})
        try:
            response = self.client.chat.completions.create(
                model=self.openai_model, messages=self.history
            )
            self.history.append({"role": "assistant", "content": response.choices[0].message.content})
        except Exception as e:
            self.history.append({"role": "assistant", "content": ""})
    def chat_history(self):
        return self.history
