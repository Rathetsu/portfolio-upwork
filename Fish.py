import streamlit as st

from utils import OPENAI_API_KEY
from openai import OpenAI
import json


class RedFish:
    def __init__(self) -> None:
        pass


class BlueFish:
    def __init__(self) -> None:
        pass


class BothFish:
    def __init__(self) -> None:
        pass


class Fishbot:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=OPENAI_API_KEY())
        self.set_init()

    def set_init(self):
        if "fish_chat_message" not in st.session_state:
            st.session_state.fish_chat_message = {
                "messages": [
                    {
                        "role": "system",
                        "content": """
                        You are a dramatic responser of fishes. 
                        Respond to user's prompt representing fishes.
                        
                        Must remember and follow 7 rules.
                        1. Response must be short and dramatic and childish.
                        2. There are only 2 fishes, Nemo and Dory.
                        3. The feature of Nemo starts with [[[ and ends with ]]]
                        4. The feature of Dory starts with <<< and ends with >>>
                        5. Respond naturally and dramatically.
                        6. Must call get_fish_response and response either of fishes.
                        7. If the user doesn't mention name for greetings, respond for both, for example, if the user says 'Hi', then both of Nemo and Dory respond greetings.
                        
                        Here's the feature of Nemo fish.
                        [[[
                        name : Nemo,
                        age : 6,
                        gender : female,
                        color : red,
                        size : fat,
                        habit : singing
                        ]]]
                        
                        Here's the feature of Dory fish.
                        <<<
                        name : Dory,
                        age : 3,
                        gender : male,
                        color : blue,
                        size : thin,
                        habit : dancing
                        >>>
                        """,
                    },
                    {
                        "role": "user",
                        "content": "Hi",
                    },
                    {
                        "role": "assistant",
                        "content": "Nemo's reply : Hi, I'm Nemo.\n\
                                     Dory's reply : Hi, I'm Dory.",
                    },
                ]
            }
        self.tools = [
            {
                "type": "function",
                "function": {
                    "name": "get_fish_response",
                    "description": """Get the response that represents either of Nemo and Dory. """,
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "red_response": {
                                "type": "string",
                                "description": "A dramatic and simple response from Nemo that brings pleasure to the user. If the user doesn't mention the name, respond to the user in any way. For example, if the user says Hi, must respond greetings. For example, user : 'hi', then returns 'Hi, I'm Nemo'",
                            },
                            "blue_response": {
                                "type": "string",
                                "description": "A dramatic and simple response from Dory that brings pleasure to the user. If the user doesn't mention the name, respond to the user in any way. For example, if the user says Hi, must respond greetings. For example, user : 'hi', then returns 'Hi, I'm Dory'",
                            },
                        },
                    },
                    "required": ["red_response", "blue_response"],
                },
            }
        ]
        self.messages = st.session_state.fish_chat_message["messages"]

    def append_message(self, msg, role):
        self.messages.append({"role": role, "content": msg})

    def ask(self, user_query):
        self.append_message(user_query, "user")
        for _ in range(0, 4):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=self.messages,
                    tools=self.tools,
                    tool_choice="auto",  # auto is default, but we'll be explicit
                )
                print("\n\n\n\n****\n\n\n\n")
                print(self.messages)

                response_message = response.choices[0].message
                print(response_message)

                tool_calls = response_message.tool_calls
                if tool_calls:
                    for tool_call in tool_calls:
                        function_name = tool_call.function.name
                        function_args = json.loads(tool_call.function.arguments)
                        red_response = function_args.get("red_response", "")
                        blue_response = function_args.get("blue_response", "")

                        response_chat = ""
                        if red_response:
                            response_chat += f"Nemo's reply : {red_response}"
                        if blue_response:
                            response_chat += f"Dory's reply : {blue_response}"

                        self.append_message(response_chat, "assistant")

                        return red_response, blue_response, None
                if response_message:
                    self.append_message(response_message, "assistant")
                    return "", "", response_message.content
                return "", "", ""
            except Exception as e:
                print(e)
                continue
        return "", "", ""
