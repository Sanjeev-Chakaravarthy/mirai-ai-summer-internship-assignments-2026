import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

st.set_page_config(
    page_title="The Memory Vault",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 The Memory Vault")
st.write("A stateful chatbot that actually remembers what you said!")
st.caption("Built using Streamlit Session State and Google Gemini API.")

st.divider()

# ----------------------------
# Sidebar - Personality Selector & Clear Button
# ----------------------------
with st.sidebar:
    st.header("Chat Settings")

    personality = st.selectbox(
        "Choose a Personality",
        [
            "🟢 Master Yoda",
            "🔴 Deadpool",
            "🏴‍☠️ Captain Jack Sparrow",
            "🎤 Stand-up Comedian",
            "🕵️ Sherlock Holmes",
        ],
        index=None,
        placeholder="Select from the list"
    )

    st.divider()

    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# ----------------------------
# API Client
# ----------------------------
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# ----------------------------
# TASK 1: Initialize the Memory Vault
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# TASK 2: Render Chat History
# ----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Personality guard
# ----------------------------
if not personality:
    st.info("👈 Please choose a personality from the sidebar to start chatting.")
else:
    # ----------------------------
    # TASK 3: Chat Input (walrus operator)
    # ----------------------------
    if user_message := st.chat_input("Say something..."):

        # ----------------------------
        # TASK 4: Save & display user message
        # ----------------------------
        st.session_state.messages.append(
            {"role": "user", "content": user_message}
        )
        with st.chat_message("user"):
            st.markdown(user_message)

        # Build prompt with personality
        prompt = f"""
        You are {personality}.
        Reply naturally while staying completely in character.
        Keep your responses engaging and consistent with the selected personality.
        User:
        {user_message}
        """

        try:
            with st.spinner("Thinking..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                ai_response = response.text

                # ----------------------------
                # TASK 4: Save & display AI response
                # ----------------------------
                st.session_state.messages.append(
                    {"role": "assistant", "content": ai_response}
                )
                with st.chat_message("assistant"):
                    st.markdown(ai_response)

        except Exception as e:
            st.error("Unable to connect to Gemini. Please try again.")

st.divider()
st.caption("Built with ❤️ using Streamlit • MirAI Summer Internship 2026")
