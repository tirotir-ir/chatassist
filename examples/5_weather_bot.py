from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
response = api.send_message("Tell me about today's weather in New York City.")
print(f"Weather Bot: {response}")
