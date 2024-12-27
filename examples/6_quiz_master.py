from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
response = api.send_message("Give me a trivia question.")
print(f"Quiz Bot: {response}")
