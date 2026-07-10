# Assignment 3 - The AI Multiverse

## Objective

Build an AI-powered chatbot application that:

- Lets users chat with different AI personalities
- Maintains conversation history within a session
- Integrates with the Google Gemini API
- Manages API keys securely using environment variables

---

## Features

- ✅ Multiple AI Personalities (Yoda, Deadpool, Jack Sparrow, Comedian, Sherlock)
- ✅ Persistent Conversation History (within session)
- ✅ Sidebar for Personality Selection
- ✅ Clear Conversation Button
- ✅ Secure API Key Management via `.env`
- ✅ Error Handling for API Failures
- ✅ Clean Streamlit Chat Interface

---

## Technologies Used

- Python
- Streamlit
- Google Gemini API (`google-genai`)
- python-dotenv

---

## Project Structure

```text
Assignment-3/
│
├── assignment2.py
├── requirements.txt
├── README.md
├── .env
└── screenshots/
```

---

## How to Run

1. Install the required packages

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project folder

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

3. Run the application

```bash
streamlit run assignment2.py
```

---

## 📸 Screenshots

### 🏠 Home Screen

Displays the initial chat interface with the personality selector in the sidebar.

![Home Screen](screenshots/home.png)

---

### 💬 Conversation Example

Shows an active conversation with one of the AI personalities.

![Conversation](screenshots/chat.png)

---

## Concepts Covered

- Streamlit UI & Chat Interface
- Google Gemini API Integration
- Prompt Engineering & AI Personalities
- Session State Management
- Environment Variables & API Key Security
- Error Handling

---

*Built as part of the MirAI School of Technology Virtual Summer Internship 2026.*
