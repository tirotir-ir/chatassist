from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = api.send_message(user_input)
    print(f"ChatGPT: {response}")
