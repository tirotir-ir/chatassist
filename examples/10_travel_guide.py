from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
city = "Paris"
response = api.send_message(f"What are some must-visit places in {city}?")
print(f"Travel Guide: {response}")
