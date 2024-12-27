import requests
import os
import time
from requests.exceptions import RequestException


class ChatGPTAPI:
    def __init__(
        self,
        api_key=None,
        api_key_path="api_key.txt",
        model="gpt-3.5-turbo",
        proxies=None,
    ):
        """
        Initialize the API client with an API key and optional proxy support.
        """
        self.api_key = api_key or self._load_api_key(api_key_path)
        self.model = model
        self.base_url = "https://api.openai.com/v1/chat/completions"
        self.proxies = proxies

    def _load_api_key(self, path):
        """
        Load the API key from a file.
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"API key file not found at {path}")
        with open(path, "r") as file:
            return file.read().strip()

    def send_message(
        self,
        message,
        temperature=0.7,
        max_tokens=1000,
        top_p=1.0,
        max_retries=3,
    ):
        """
        Send a message to the ChatGPT API with customizable parameters.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": message}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
        }

        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.base_url,
                    json=payload,
                    headers=headers,
                    proxies=self.proxies,  # Add proxy support
                )
                response.raise_for_status()
                return response.json()["choices"][0]["message"]["content"]
            except RequestException as e:
                if attempt < max_retries - 1:
                    time.sleep(2**attempt)  # Exponential backoff
                else:
                    raise e
