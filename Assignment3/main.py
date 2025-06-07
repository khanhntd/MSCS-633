from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot instance
chatbot = ChatBot('TerminalBot')

# Training with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")

# start_chat will start a command line and initiate a chat conversation with the chatbot
def start_chat():
    print("Hello! I am TerminalBot. Type 'exit' to end the chat.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Goodbye!")
                break
            response = chatbot.get_response(user_input)
            print("Bot:", response)
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

if __name__ == '__main__':
    start_chat()