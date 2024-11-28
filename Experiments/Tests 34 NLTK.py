import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']],
    ['how are you?', ['I am doing well, thank you!', 'Iam good, thanks for asking. How about you?']],
    ['(.*) your name?', ['My name is ChatBot.', "I'm ChatBot, nice to meet you!"]],
    ['(.*) (age|old) are you?', ["I'm a computer program, so I don't have an age."]],
    ['(.*) (created|made) you?', ["I was created by a team of developers.", "I'm the result of some coding magic!"]],
    ['(.*) (help|assistance)', ["Sure, I'll do my best to help you.", "How can I assist you?"]],
    ['(.*)', ["I'm sorry, I didn't understand that.", "Could you please rephrase?"]],
]

# Create a ChatBot instance
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hello! I'm ChatBot. Let's chat. Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
