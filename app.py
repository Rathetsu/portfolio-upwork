import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import json
from streamlit_chat import message
from streamlit_elements import elements, mui, html

from utils import CSS_STYLE, chat_ui, is_system_prompt

from iconfig import DEVELOPER_NAME

from chatbot import CustomerDataChatbot

customer_bot = CustomerDataChatbot()

st.set_page_config(
    page_title=DEVELOPER_NAME, layout="wide", initial_sidebar_state="collapsed"
)

# Data Pull and Functions
st.markdown(
    CSS_STYLE,
    unsafe_allow_html=True,
)


@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


with st.sidebar:
    selected = option_menu(
        DEVELOPER_NAME,
        ["Intro", "About"],
        icons=["play-btn", "info-circle"],
        menu_icon="heart",
        default_index=0,
    )


def on_btn_click():
    del st.session_state.past[:]
    del st.session_state.generated[:]


if selected == "Intro":
    from iconfig import (
        DEVELOPER_ROLE,
        DEVELOPER_PASSION,
        DEVELOPER_GREETINGS,
        DEVELOPER_INTRODUCTION,
        DEVELOPER_SKILLS,
        DEVELOPER_EXPERIENCE_VIDEO,
        DEVELOPER_EXPERIENCE_TITLE,
        DEVELOPER_EXPERIENCE_IMAGE,
        DEVELOPER_VIDEO_INTRODUCTION,
        DEVELOPER_EXPERIENCE_YEARS,
    )

    col1, col2 = st.columns([6, 2])
    with col1:

        st.title(DEVELOPER_ROLE)
        st.subheader(DEVELOPER_PASSION)

        with st.columns([1, 3, 1])[1]:
            lottie = load_lottiefile("assets/develop1.json")
            st_lottie(lottie, key="develop1")

        st.header(DEVELOPER_GREETINGS)
        st.markdown(DEVELOPER_INTRODUCTION)
        st.divider()

        cols = st.columns(len(DEVELOPER_SKILLS))
        for index, col in enumerate(cols):
            with col:
                st.subheader(DEVELOPER_SKILLS[index][0])
                with st.container(height=60):
                    st.caption(DEVELOPER_SKILLS[index][1])
                st.write(DEVELOPER_SKILLS[index][2])
                st.caption(DEVELOPER_SKILLS[index][3])
                st.write(DEVELOPER_SKILLS[index][4])
                st.caption("- " + "\n- ".join(DEVELOPER_SKILLS[index][5]))

        st.divider()
        st.subheader(DEVELOPER_EXPERIENCE_TITLE)
        cols = st.columns(len(DEVELOPER_EXPERIENCE_IMAGE))
        for index, col in enumerate(cols):
            with col:
                st.image(
                    DEVELOPER_EXPERIENCE_IMAGE[index][0],
                    caption=DEVELOPER_EXPERIENCE_IMAGE[index][1],
                )

        # st.divider()
        # st.subheader(DEVELOPER_VIDEO_INTRODUCTION)
        # for index, video in enumerate(DEVELOPER_EXPERIENCE_VIDEO):
        #     st.video(DEVELOPER_EXPERIENCE_VIDEO[index][-1])

        # import pandas as pd
        # import numpy as np

        # chart_data = pd.DataFrame(
        #     {
        #         "skill": [item[0] for item in DEVELOPER_EXPERIENCE_YEARS],
        #         "years": [item[1] for item in DEVELOPER_EXPERIENCE_YEARS],
        #     }
        # )
        # st.bar_chart(
        #     chart_data,
        #     x="skill",
        #     y=["years"],
        #     color=["#0068C9"],
        #     height = 500,
        # )
    with st.expander("", True):
        chat_placeholder = st.empty()

        messages = chat_placeholder.container(height=300)
        prompt = st.chat_input("Say something")
        if prompt:
            customer_bot.ask(prompt)
        messages_history = customer_bot.chat_history()
        with messages:
            for msg in messages_history:
                if not is_system_prompt(msg["role"], msg["content"]):
                    with st.container():
                        st.write(
                            chat_ui(msg["role"], msg["content"]), unsafe_allow_html=True
                        )
