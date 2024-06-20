import streamlit as st
import base64

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        # Read the image file in binary mode
        encoded_string = base64.b64encode(image_file.read())
        # Encode the binary data as a base64 string
        return "data:image/png; base64," + encoded_string.decode("utf-8")


CSS_STYLE = (
    """
<style>
.big-font {
    font-size:80px !important;
}
div[data-testid='stVerticalBlockBorderWrapper'] {
    border : none !important;
    padding : 0 !important;
}
div[data-testid='stExpander'] {
    position : fixed;
    right : 30px;
    bottom : 5vh;
    width : 500px;
    # height : 400px;
    max-width : 90vw;
    # min-height : 46vh;
}
div[data-testid='stExpander'] details {
    padding-bottom: 1.5rem !important;
    border-radius : 2rem;
    background-color: #1C2E46;
}
div[data-testid='stExpander'] div[data-testid='stExpanderDetails'] {
    padding: 0 !important;
}
div[data-testid='stExpander'] div[data-testid='stVerticalBlock'] {
    border-radius : 0.5rem;
}
div[data-testid='stExpander'] div[data-testid='stVerticalBlock'] > div[data-testid='stVerticalBlockBorderWrapper'] {
    # vertical-align: middle;
    border-color: transparent !important;
    background-color:white;
    border-radius : 2rem;
    margin-bottom: 0.5rem;
    padding : 0.5rem !important;
}
div[data-testid='stExpander'] div[data-baseweb='textarea'] {
    background-color : #192A3F;
    border-color : #192A3F;
    border-radius : 0.4rem;
}
div[data-testid='stExpander'] div .stChatInput {
    width : 90% !important;
    margin: auto;
}
div[data-testid='stExpander'] div.stChatInput > div:first-child {
    width: 90%;
}
div[data-testid='stExpander'] div.containAssistant {
    
}
div[data-testid='stExpander'] div.containUser {
    display: flex;
    justify-content: flex-end;
}
div[data-testid='stExpander'] div.chatAssistant {
    max-width : 80% !important;
    color : #454545;
    display: flex;
    flex-direction: row;
}
"""
    + f"""
div[data-testid='stExpander'] div.chatAssistant > img {{
    min-width : 40px;
    min-height : 40px;
    max-width : 40px;
    max-height : 40px;
    background-image: url('{image_to_base64("assets/profile.png")}');
    background-size: contain;
    background-repeat: no-repeat;
    border-radius : 50%;
}}"""
    + """
div[data-testid='stExpander'] div.chatAssistant > div {
    margin : 0.5rem;
}
div[data-testid='stExpander'] div.chatUser {
    max-width : 60%;
    text-align : right;
    color : white;
    background-color : #1C2E46;
    padding : 0.5rem;
    border-radius : 1rem 1rem 0 1rem;
}
</style>
"""
)

def is_system_prompt(role, content):
    if role == "system":
        return True
    return False

def chat_ui(role, content):
    if role == "assistant":
        return f"<div class = 'containAssistant'><div class = 'chatAssistant'><img></img><div>{content}</div></div></div>"
    if role == "user":
        return (
            f"<div class = 'containUser'><div class = 'chatUser'>{content}</div></div>"
        )
