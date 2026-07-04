print("=== AI Chatbot ===")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hello!")
    elif user == "how are you":
        print("Bot: I am fine.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: I don't understand.")