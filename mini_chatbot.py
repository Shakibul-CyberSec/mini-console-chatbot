from dotenv import load_dotenv
import os
import requests
from colorama import Fore, Style, init

# Initialize colorama for colored console output
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
url = "https://api.groq.com/openai/v1/chat/completions"

# Initialize chat history with system role
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

while True:
    # Get user input
    user_input = input(Fore.BLUE + "You: " + Style.RESET_ALL)
    
    # Exit chat if user types 'exit'
    if user_input.lower() == "exit":
        print(Fore.YELLOW + "Chat ended. Goodbye!" + Style.RESET_ALL)
        break

    # Append user message to chat history
    messages.append({"role": "user", "content": user_input})

    # Prepare API request
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "max_tokens": 150
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Call Groq API
    response = requests.post(url, headers=headers, json=data)
    resp_json = response.json()

    # Check if API returned a valid response
    if "choices" in resp_json:
        reply = resp_json["choices"][0]["message"]["content"]
        # Print AI response in green
        print(Fore.GREEN + "AI: " + Style.RESET_ALL + reply)
        # Append AI response to chat history
        messages.append({"role": "assistant", "content": reply})
    else:
        # Print API error in red
        print(Fore.RED + "API Error: " + str(resp_json) + Style.RESET_ALL)
