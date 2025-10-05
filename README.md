# Groq Python Chatbot

A **mini console-based chatbot** built in **Python** and integrated with the **Groq API**.  
Supports **colored terminal output**, conversation memory, and smooth interactive chatting.

---

## Features

- Built with Python 3.x
- Integrated with Groq API (llama-3.1-8b-instant)
- Interactive console chatbot
- Maintains chat history
- Colorized output using [colorama](https://pypi.org/project/colorama/)
- Easy to run and extend
- Exit chat gracefully with `exit` command

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Shakibul-CyberSec/mini-console-chatbot.git
cd mini-console-chatbot
```
2. **Create a virtual environment (optional but recommended)**
```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
3.**Install dependencies**
```
pip install -r requirements.txt
```
4.**Set up your Groq API key**
- You can get you api key from [here](https://console.groq.com/keys).
- Create a .env file in the project root:
```
GROQ_API_KEY=your_api_key_here
```
## Usage
Run the chatbot:
```
python3 mini_chatbot.py
```
- Type your messages and press Enter
- Type exit to quit the chat

## Dependencies

- [requests](https://pypi.org/project/requests/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [colorama](https://pypi.org/project/colorama/)
