import tkinter as tk
from tkinter import simpledialog, messagebox
from chatassist.api import ChatGPTAPI
from chatassist.utils import load_api_key

def run_question_gui():
    # Load the API key
    api_key = load_api_key("api_key.txt")
    api = ChatGPTAPI(api_key=api_key)

    # Create the main window
    root = tk.Tk()
    root.title("ChatGPT - FAQ Bot")

    # Add a text widget to display questions and answers
    output_area = tk.Text(root, state="disabled", wrap="word", height=20, width=60)
    output_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Add an entry field for questions
    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=5, fill=tk.X)

    question_input = tk.Entry(input_frame)
    question_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

    def add_question():
        # Get the question from the input field
        question = question_input.get()
        if not question:
            return
        question_input.delete(0, tk.END)

        # Send the question to ChatGPT and get the answer
        try:
            response = api.send_message(question)
            output_area.config(state="normal")
            output_area.insert(tk.END, f"Q: {question}\nA: {response}\n\n")
            output_area.config(state="disabled")
            output_area.see(tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")

    # Add a button to submit questions
    send_button = tk.Button(input_frame, text="Ask", command=add_question)
    send_button.pack(side=tk.RIGHT)

    root.mainloop()

if __name__ == "__main__":
    run_question_gui()
