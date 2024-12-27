
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
from chatassist.api import ChatGPTAPI
from chatassist.conversation import Conversation

def run_gui():
    # Initialize the main application window
    root = tk.Tk()
    root.title("ChatGPT GUI")

    # Initialize API and conversation
    api_key = simpledialog.askstring("API Key", "Enter your OpenAI API Key:")
    if not api_key:
        messagebox.showerror("Error", "API Key is required.")
        return

    api = ChatGPTAPI(api_key=api_key)
    conversation = Conversation()

    # Add text display for chat history
    chat_display = tk.Text(root, state="disabled", wrap="word")
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Add input box and send button
    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=10, fill=tk.X)

    user_input = tk.Entry(input_frame)
    user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

    def send_message():
        message = user_input.get()
        if not message:
            return
        user_input.delete(0, tk.END)

        # Display user message
        conversation.add_message("user", message)
        chat_display.config(state="normal")
        chat_display.insert(tk.END, f"You: {message}\n")
        chat_display.config(state="disabled")
        chat_display.see(tk.END)

        # Send to API and display response
        try:
            response = api.send_message(message)
            conversation.add_message("assistant", response)
            chat_display.config(state="normal")
            chat_display.insert(tk.END, f"ChatGPT: {response}\n")
            chat_display.config(state="disabled")
            chat_display.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    def export_conversation():
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            conversation.save_to_file(file_path)

    def load_conversation():
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            conversation.load_from_file(file_path)
            chat_display.config(state="normal")
            chat_display.delete(1.0, tk.END)
            for msg in conversation.get_history():
                chat_display.insert(tk.END, f"{msg['role'].capitalize()} ({msg['timestamp']}): {msg['content']}\n")
            chat_display.config(state="disabled")
            chat_display.see(tk.END)

    send_button = tk.Button(input_frame, text="Send", command=send_message)
    send_button.pack(side=tk.RIGHT)

    menu = tk.Menu(root)
    root.config(menu=menu)

    file_menu = tk.Menu(menu, tearoff=0)
    file_menu.add_command(label="Export Conversation", command=export_conversation)
    file_menu.add_command(label="Load Conversation", command=load_conversation)
    menu.add_cascade(label="File", menu=file_menu)

    root.mainloop()

if __name__ == "__main__":
    run_gui()
