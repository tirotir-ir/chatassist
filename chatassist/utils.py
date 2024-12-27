import os


def format_response(response):
    """
    Format the API response for display.
    """
    if "choices" in response and len(response["choices"]) > 0:
        return response["choices"][0]["message"]["content"]
    return ""


def validate_api_key(api_key):
    """
    Validate the provided API key.
    """
    if not api_key or not isinstance(api_key, str) or len(api_key) < 10:
        raise ValueError("Invalid API key.")


def load_api_key(path="api_key.txt"):
    """
    Load the API key from a specified file path.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"API key file not found at {path}")
    with open(path, "r") as file:
        return file.read().strip()
