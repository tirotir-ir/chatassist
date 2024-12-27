
import time
import json

class Conversation:
    def __init__(self):
        """
        Initialize a new conversation instance.
        """
        self.history = []

    def add_message(self, role, content):
        """
        Add a message to the conversation history.
        """
        self.history.append({
            "role": role,
            "content": content,
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S')
        })

    def save_to_file(self, path):
        """
        Save the conversation history to a file.
        """
        with open(path, 'w') as file:
            json.dump(self.history, file, indent=4)

    def load_from_file(self, path):
        """
        Load conversation history from a file.
        """
        with open(path, 'r') as file:
            self.history = json.load(file)

    def get_history(self):
        """
        Retrieve the conversation history.
        """
        return self.history
