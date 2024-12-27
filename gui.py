import tkinter as tk
from tkinter import messagebox, filedialog
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key
from chatassist.conversation import Conversation


def run_gui():
    # Load the API key from api_key.txt
    try:
        api_key = load_api_key("api_key.txt")
    except FileNotFoundError:
        messagebox.showerror(
            "Error",
            "API key file (api_key.txt) not found.",
            "Please create the file with your API key.",
        )
        return
    except ValueError:
        messagebox.showerror(
            "Error",
            "Invalid API key.",
            "Please ensure the API key in api_key.txt is correct.",
        )
        return

    api = ChatGPTAPI(api_key=api_key)
    conversation = Conversation()

    # Create the main application window
    root = tk.Tk()
    root.title("ChatAssist - Enhanced Chat GUI")
    root.geometry("600x700")  # Set default size

    # Configure row/column weights for resizing
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Frame for chat display
    chat_frame = tk.Frame(root, padx=10, pady=10)
    chat_frame.grid(row=0, column=0, sticky="nsew")

    # Scrollable chat display
    chat_display = tk.Text(
        chat_frame,
        wrap="word",
        state="disabled",
        bg="#f5f5f5",
        fg="#333333",
        font=("Arial", 12),
    )
    chat_display.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    # Scrollbar for the chat display
    chat_scrollbar = tk.Scrollbar(chat_frame, command=chat_display.yview)
    chat_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_display["yscrollcommand"] = chat_scrollbar.set

    # Frame for user input
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.grid(row=1, column=0, sticky="ew")
    input_frame.columnconfigure(0, weight=1)

    # Entry field for user input
    user_input = tk.Entry(input_frame, font=("Arial", 12))
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
            conversation.add_message("user", message)
            conversation.add_message("assistant", response)
            chat_display.config(state="normal")
            chat_display.insert(
                tk.END, f"ChatAssist: {response}\n\n", "chatgpt_response"
            )
            chat_display.config(state="disabled")
            chat_display.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    # Send button to trigger the send_message function
    send_button = tk.Button(input_frame, text="Send", command=send_message)
    send_button.grid(row=0, column=1)

    # Style tags for the chat display
    chat_display.tag_config(
        "user_message", foreground="#1a73e8", font=("Arial", 12, "bold")
    )
    chat_display.tag_config(
        "chatgpt_response", foreground="#555555", font=("Arial", 12)
    )

    # Menu for saving and loading conversations
    def export_conversation():
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            conversation.save_to_file(file_path)

    def load_conversation():
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json")]
        )
        if file_path:
            conversation.load_from_file(file_path)
            chat_display.config(state="normal")
            chat_display.delete(1.0, tk.END)
            for msg in conversation.get_history():
                chat_display.insert(
                    tk.END,
                    f"{msg['role'].capitalize()} "
                    f"({msg['timestamp']}): "
                    f"{msg['content']}\n",
                )
            chat_display.config(state="disabled")
            chat_display.see(tk.END)

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    file_menu.add_command(
        label="Export Conversation", command=export_conversation
    )
    file_menu.add_command(label="Load Conversation", command=load_conversation)
    menu.add_cascade(label="File", menu=file_menu)

    # Start the GUI main loop
    root.mainloop()


if __name__ == "__main__":
    run_gui()
