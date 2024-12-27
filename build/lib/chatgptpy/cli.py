
import argparse
import json
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

def main():
    """
    Command-line interface for interacting with ChatGPT.
    """
    parser = argparse.ArgumentParser(description="ChatGPT CLI")
    parser.add_argument("message", type=str, help="Message to send to ChatGPT")
    parser.add_argument("--api-key-path", type=str, default="api_key.txt", help="Path to API key file")
    parser.add_argument("--temperature", type=float, default=0.7, help="Response randomness (0.0-1.0)")
    parser.add_argument("--export", type=str, help="Path to export conversation history (JSON format)")

    args = parser.parse_args()

    # Load API key
    api_key = load_api_key(args.api_key_path)

    # Initialize ChatGPT API
    api = ChatGPTAPI(api_key=api_key)

    # Send message and get response
    try:
        response = api.send_message(args.message, temperature=args.temperature)
        print(f"ChatGPT: {response}")

        # Export conversation if specified
        if args.export:
            with open(args.export, "w") as file:
                history = [{"role": "user", "content": args.message}, {"role": "assistant", "content": response}]
                json.dump(history, file, indent=4)
            print(f"Conversation history exported to {args.export}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
