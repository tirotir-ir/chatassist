from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
word = "serendipity"
response = api.send_message(f"Define the word: {word}.")
print(f"Dictionary Bot: {response}")
