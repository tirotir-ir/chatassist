
# ChatAssist

An advanced Python library for handling ChatGPT interactions.

---

## **Features**

- **Save and Resume Conversations**: Save conversation history to a file and reload it later.
- **Proxy Support**: Send API requests through a user-defined proxy.
- **Configurable Parameters**: Customize settings like `temperature`, `top_p`, and `max_tokens`.
- **Stream Output**: Display responses incrementally as they are generated.
- **Command-Line Interface**: Quickly interact with ChatGPT from the terminal.
- **Graphical User Interface**: User-friendly GUI for non-technical users.
- **Markdown Rendering in GUI**: Display formatted text and code blocks in responses.
- **Built-in Logging**: Log all interactions for debugging or auditing purposes.
- **Dynamic Model Selection**: Switch between models like GPT-3.5-Turbo or GPT-4.

---

## **Installation**

### **From Source**

Install the library from the source code:

```bash
pip install .
```

For development mode:

```bash
pip install -e .
```

### **Verify Installation**

Run this command to verify:

```bash
python -c "import chatassist; print(chatassist.__version__)"
```

You should see the version number printed.

---

## **Usage**

### **Python API**

The `ChatAssist` library provides a simple API for interacting with ChatGPT.

```python
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

# Load the API key
api_key = load_api_key("api_key.txt")

# Initialize the ChatGPT API client
api = ChatGPTAPI(api_key=api_key)

# Send a message
response = api.send_message("Hello, ChatGPT!")
print(response)
```

### **Saving and Resuming Conversations**

Use the `Conversation` class to manage chat histories:

```python
from chatassist.conversation import Conversation

conversation = Conversation()
conversation.add_message("user", "Hello!")
conversation.add_message("assistant", "Hi there! How can I assist you?")

# Save to a file
conversation.save_to_file("conversation.json")

# Reload the conversation
loaded_conversation = Conversation()
loaded_conversation.load_from_file("conversation.json")
print(loaded_conversation.get_history())
```

### **Using Proxies**

Pass a proxy configuration to route API requests through a proxy server:

```python
api = ChatGPTAPI(api_key=api_key, proxies={"http": "http://proxy.example.com:8080"})
response = api.send_message("What is Python?")
print(response)
```

---

## **Command-Line Interface**

The CLI allows you to interact with ChatGPT directly from the terminal.

### **Basic Usage**

```bash
chatassist-cli "What is the capital of France?" --api-key-path api_key.txt
```

### **Export Conversation**

Save the conversation to a file:

```bash
chatassist-cli "Tell me about Python." --export conversation.json
```

---

## **Graphical User Interface**

The GUI provides an intuitive way to interact with ChatGPT.

### **Launching the GUI**

Run the following command:

```bash
python -m chatassist.gui
```

### **Features**

1. **Type and Send Messages**:
   - Enter your message in the input field and press "Send".
   - Responses are displayed in the chat window.

2. **Save and Load Conversations**:
   - Export the conversation to a file for later use.
   - Reload previous conversations using the "Load Conversation" option.

---

## **Configuration Parameters**

The `ChatAssist` API allows you to fine-tune interactions with the following parameters:

- **`temperature`**: Controls the randomness of responses.
- **`top_p`**: Limits responses to the top tokens in cumulative probability.
- **`max_tokens`**: Restricts the number of tokens in the response.
- **`model`**: Allows you to switch between models, e.g., `gpt-3.5-turbo` or `gpt-4`.

```python
response = api.send_message(
    "Tell me about AI.",
    temperature=0.5,
    top_p=0.8,
    max_tokens=500
)
print(response)
```

---

## **Practical Examples**

### **1. Simple FAQ Bot**

```python
questions = ["What is Python?", "What is AI?", "Who created ChatGPT?"]
for question in questions:
    response = api.send_message(question)
    print(f"Q: {question}
A: {response}
")
```

### **2. Programming Assistant**

```python
prompt = "Explain the concept of recursion with a Python example."
response = api.send_message(prompt)
print(response)
```

### **3. Travel Guide**

```python
prompt = "What are the best tourist attractions in Paris?"
response = api.send_message(prompt)
print(response)
```

### **4. Math Solver**

```python
problem = "What is the result of 123 * 456?"
response = api.send_message(problem)
print(response)
```

### **5. Language Translator**

```python
prompt = "Translate 'Hello, how are you?' into Spanish."
response = api.send_message(prompt)
print(response)
```

---

## **Testing**

### **Run All Tests**

Navigate to the `tests/` directory and run:

```bash
python -m unittest discover tests
```

### **Verify Individual Tests**

To run a specific test file:

```bash
python tests/test_api.py
```

---
## Steps to Run Examples

1. Clone the repository:
```bash
git clone https://github.com/tirotir-ir/chatassist.git
cd chatassist
```
2. Create and fill the api_key.txt file with your OpenAI API key:
```bash
echo "your-openai-api-key" > api_key.txt
```
Replace your-openai-api-key with your actual API key. 
This file is required for running the examples and communicating with the OpenAI API.

3. Navigate to the examples/ directory:

```bash
cd examples
```
‍‍‍‍‍‍‍4. Run an example script:
‍‍‍
```bash
    python 14_advanced_chatbot_gui.py
```
Replace 14_advanced_chatbot_gui.py with the desired example script from the examples/ directory.
---
## **Troubleshooting**

### **Common Issues**

- **API Key Not Found**:
  - Ensure the `api_key.txt` file exists and contains a valid API key.
- **Module Not Found**:
  - Verify the library is installed using `pip show chatassist`.

### **Debugging**

Enable detailed logging by adding:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## **License**

This project is licensed under the MIT License.

---

## **Contact and Support**

For questions or support, please raise an issue on the project repository or contact the maintainer.
