from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

api_key = load_api_key("api_key.txt")
api = ChatGPTAPI(api_key=api_key)
problem = "What is 12 multiplied by 8?"
response = api.send_message(problem)
print(f"Math Solver: {response}")
