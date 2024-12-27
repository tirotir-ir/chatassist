import tkinter as tk
from tkinter import messagebox, ttk
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

def run_advanced_chatbot_gui():
    # Load the API key
    try:
        api_key = load_api_key("api_key.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load API key: {e}")
        return

    api = ChatGPTAPI(api_key=api_key)

    # Create the main application window
    root = tk.Tk()
    root.title("ChatGPT - Advanced Chatbot")
    root.geometry("600x700")  # Set default window size

    # Configure row/column weights for resizing
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Frame for chat display
    chat_frame = tk.Frame(root, padx=10, pady=10)
    chat_frame.grid(row=0, column=0, sticky="nsew")

    # Scrollable chat display
    chat_display = tk.Text(chat_frame, wrap="word", state="disabled", bg="#f5f5f5", fg="#333333", font=("Arial", 12))
    chat_display.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    # Scrollbar for the chat display
    chat_scrollbar = ttk.Scrollbar(chat_frame, command=chat_display.yview)
    chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_display["yscrollcommand"] = chat_scrollbar.set

    # Frame for user input
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.grid(row=1, column=0, sticky="ew")
    input_frame.columnconfigure(0, weight=1)

    # Entry field for user input
    user_input = ttk.Entry(input_frame, font=("Arial", 12))
    user_input.grid(row=0, column=0, sticky="ew", padx=(0, 10))

    # Function to send the user message to ChatGPT
    def send_message():
        message = user_input.get().strip()
        if not message:
            return

        # Display the user message in the chat display
        chat_display.config(state="normal")
        chat_display.insert(tk.END, f"You: {message}\n", "user_message")
        chat_display.config(state="disabled")
        chat_display.see(tk.END)
        user_input.delete(0, tk.END)

        # Get ChatGPT's response
        try:
            response = api.send_message(message)
            chat_display.config(state="normal")
            chat_display.insert(tk.END, f"ChatGPT: {response}\n\n", "chatgpt_response")
            chat_display.config(state="disabled")
            chat_display.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    # Send button to trigger the send_message function
    send_button = ttk.Button(input_frame, text="Send", command=send_message)
    send_button.grid(row=0, column=1)

    # Style tags for the chat display
    chat_display.tag_config("user_message", foreground="#1a73e8", font=("Arial", 12, "bold"))
    chat_display.tag_config("chatgpt_response", foreground="#555555", font=("Arial", 12))

    # Main event loop
    root.mainloop()

if __name__ == "__main__":
    run_advanced_chatbot_gui()
