import nltk
import json
from nltk.chat.util import Chat, reflections

conversation = json.load(open("conversation.json"))

def start():
    print("Welcome to Miru Chatbot | Build use nltk")
    chat = Chat(conversation, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    start()