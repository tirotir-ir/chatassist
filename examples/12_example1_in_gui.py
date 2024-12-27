import tkinter as tk
from tkinter import messagebox
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

def run_simple_chat_gui():
    # Load the API key
    api_key = load_api_key("api_key.txt")
    api = ChatGPTAPI(api_key=api_key)

    # Create the main application window
    root = tk.Tk()
    root.title("ChatGPT - Simple Chat")

    # Add a text area to display the ChatGPT response
    output_area = tk.Text(root, state="disabled", wrap="word", height=10, width=50)
    output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def get_response():
        # Send a message to ChatGPT and display the response
        try:
            response = api.send_message("Hello, ChatGPT!")
            output_area.config(state="normal")
            output_area.insert(tk.END, f"ChatGPT: {response}\n")
            output_area.config(state="disabled")
            output_area.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    # Add a button to trigger the interaction
    send_button = tk.Button(root, text="Send 'Hello, ChatGPT!'", command=get_response)
    send_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    run_simple_chat_gui()
