import os
import sys
import textwrap
from openai import OpenAI

# Make sure your OPENAI_API_KEY environment variable is set!

client = OpenAI()

BANNER = r"""
   ____ _           _    ____ ____ _____ 
  / ___| |__   __ _| |_ / ___|  _ \_   _|
 | |   | '_ \ / _` | __| |  _| |_) || |  
 | |___| | | | (_| | |_| |_| |  __/ | |  
  \____|_| |_|\__,_|\__|\____|_|    |_|  

        Made by SpiritePVP
"""

def main_menu():
    print(BANNER)
    print("1) Set a prompt for an answer")
    print("2) Upload a file path and prompt")
    print("3) Close program")

def ask_chatgpt(prompt, file_content=None):
    full_prompt = prompt
    if file_content:
        full_prompt = f"{prompt}\n\n---\nFile content:\n{file_content}\n---"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Change model here if you want
            messages=[{"role": "user", "content": full_prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ API request failed: {e}"

def handle_prompt():
    prompt = input("\nEnter your prompt: ")
    print("\n[ChatGPT Answer]")
    answer = ask_chatgpt(prompt)
    print(textwrap.fill(answer, width=70))
    print()

def handle_file_prompt():
    path = input("\nEnter the file path: ").strip()
    if not os.path.isfile(path):
        print("❌ File not found.\n")
        return
    prompt = input("Enter your prompt: ")
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    print("\n[ChatGPT Answer with File]")
    answer = ask_chatgpt(prompt, file_content=content)
    print(textwrap.fill(answer, width=70))
    print()

def main():
    while True:
        main_menu()
        choice = input("\nChoose an option (1-3): ").strip()
        if choice == "1":
            handle_prompt()
        elif choice == "2":
            handle_file_prompt()
        elif choice == "3":
            print("\nClosing program. Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()