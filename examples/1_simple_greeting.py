from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
response = api.send_message("Hello, ChatGPT!")
print(response)  # ChatGPT responds to the greeting.
