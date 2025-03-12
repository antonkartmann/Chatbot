# Questions and answers
pairs = [
    ("hi|hello|hey|yo", ["Hello! How can I help you?"]),
    ("how are you|how are you doing", ["I'm doing great, thanks! How can I assist you?"]),
    ("what is your name", ["I am a simple chatbot, created to help you!"]),
    ("exit", ["Goodbye! Have a great day!"]),
    ("can you help me", ["Yes, of course I can help you!"]),
    ("(.*)", ["I'm not sure how to respond to that. Can you say something else?"])
]

# Function to match user input with predefined patterns
def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, responses in pairs:
        # If the input matches any of the patterns, return a response
        if any(word in user_input for word in pattern.split("|")):
            return responses[0]
    return "I'm not sure how to respond to that. Can you say something else?"

# Start conversation
print("Hello! I am your Chatbot, created by Anton Kartmann. Type 'exit' to exit the chatbot.")
while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        print("Goodbye! Have a great day!")
        break
    else:
        print(chatbot_response(user_input))
