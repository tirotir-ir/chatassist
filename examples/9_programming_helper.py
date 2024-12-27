from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
concept = "Explain recursion with examples."
response = api.send_message(concept)
print(f"Programming Helper: {response}")
