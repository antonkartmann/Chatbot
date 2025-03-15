# Questions and answers
pairs = [
    ("hi|hello|hey|yo", ["Hello! How can I help you? / Hallo! Wie kann ich dir helfen?"]),
    ("how are you|how are you doing", ["I'm doing great, thanks! How can I assist you? / Mir geht es gut, danke! Wie kann ich dir helfen?"]),
    ("what is your name", ["I am a simple chatbot, created to help you! / Ich bin ein einfacher Chatbot, der dir helfen soll!"]),
    ("exit", ["Goodbye! Have a great day! / Auf Wiedersehen! Ich wünsche dir einen schönen Tag!"]),
    ("can you help me", ["Yes, of course I can help you! / Ja, natürlich kann ich dir helfen!"]),
    ("guten morgen|moin|good morning", ["Good morning! / Guten Morgen!"]),
    ("guten abend|good evening", ["Good evening! / Guten Abend!"]),
    ("was machst du|what are you doing", ["I am here to help you! What do you need? / Ich bin hier, um dir zu helfen! Was brauchst du?"]),
    ("danke|thank you|vielen dank", ["You're welcome! / Gerne geschehen!"]),
    ("hilfe|help", ["Of course, I'd be happy to help. What do you need? / Natürlich, ich helfe dir gerne. Was brauchst du?"]),
    ("auf wiedersehen|tschüss|bye", ["Goodbye! Have a great day! / Auf Wiedersehen! Ich wünsche dir einen schönen Tag!"]),
    ("wer ist anton kartmann|who is anton kartmann", ["My developer :) / Mein Entwickler :)"]),
    ("which language do you speak|welche sprache sprichst du", ["I speak English and German. / Ich spreche Englisch und Deutsch."]),
    ("(.*)", ["I'm not sure how to respond to that. Can you say something else? / Ich bin mir nicht sicher, wie ich darauf antworten soll. Kannst du etwas anderes sagen?"])

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
