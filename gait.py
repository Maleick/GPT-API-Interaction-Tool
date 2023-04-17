import openai

openai.api_key = open("key.txt", "r").read().strip("\n")

message_history = []

def chat(inp, role="user"):
    message_history.append({"role": role, "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content

def print_help_menu():
    print("Commands:")
    print("  help          - Show this help menu")
    print("  version       - Display version information")
    print("  exit          - Exit the program")
    print("  <your_text>   - Interact with the GPT API")

def print_version_info():
    print("GPT API Interaction Tool")
    print("Version: 1.0.0")
    print("Powered by OpenAI's GPT-3.5-turbo")

print("Welcome to the GPT API Interaction Tool!")
print("Type 'help' for available commands.")
print()

while True:
    user_input = input("> ")
    
    if user_input.lower() == 'help':
        print_help_menu()
    elif user_input.lower() == 'version':
        print_version_info()
    elif user_input.lower() == 'exit':
        print("Goodbye!")
        break
    else:
        print("User's input was:", user_input)
        print(chat(user_input))
        print()
