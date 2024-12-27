import argparse
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key
from chatassist.conversation import Conversation
import sys


def main():
    """
    Command-line interface for interacting with ChatGPT.
    """
    parser = argparse.ArgumentParser(description="ChatAssist CLI")
    parser.add_argument("message", type=str, help="Message to send to ChatGPT")
    parser.add_argument(
        "--api-key-path",
        type=str,
        default="api_key.txt",
        help="Path to API key file",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.7,
        help="Response randomness (0.0-1.0)",
    )
    parser.add_argument(
        "--top-p",
        type=float,
        default=1.0,
        help="Probability mass for token selection (0.0-1.0)",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=1000,
        help="Maximum tokens in the response",
    )
    parser.add_argument(
        "--proxy",
        type=str,
        help="Proxy server URL (e.g., http://proxy.example.com:8080)",
    )
    parser.add_argument(
        "--export",
        type=str,
        help="Path to export conversation history (JSON format)",
    )

    args = parser.parse_args()

    # Load API key
    try:
        api_key = load_api_key(args.api_key_path)
    except FileNotFoundError:
        print("Error: API key file not found.", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("Error: Invalid API key.", file=sys.stderr)
        sys.exit(1)

    # Initialize ChatGPT API and conversation
    proxies = {"http": args.proxy, "https": args.proxy} if args.proxy else None
    api = ChatGPTAPI(api_key=api_key, proxies=proxies)
    conversation = Conversation()

    # Send message and get response
    try:
        response = api.send_message(
            args.message,
            temperature=args.temperature,
            top_p=args.top_p,
            max_tokens=args.max_tokens,
        )
        print(f"ChatGPT: {response}")

        # Update conversation history
        conversation.add_message("user", args.message)
        conversation.add_message("assistant", response)

        # Export conversation if specified
        if args.export:
            conversation.save_to_file(args.export)
            print(f"Conversation history exported to {args.export}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
