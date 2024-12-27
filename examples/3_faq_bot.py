from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
questions = ["What is Python?", "How do I install Python?", "What is ChatGPT?"]
for question in questions:
    print(f"Q: {question}")
    print(f"A: {api.send_message(question)}\n")
