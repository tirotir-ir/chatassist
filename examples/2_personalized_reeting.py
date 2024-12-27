from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
name = input("What is your name? ")
response = api.send_message(f"Hello, {name}! How are you today?")
print(response)
