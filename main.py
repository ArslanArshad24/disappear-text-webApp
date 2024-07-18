import tkinter as tk
from tkinter import messagebox
import threading

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")
        
        self.title_label = tk.Label(text="The Most Dangerous Writing App", font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=RED)
        self.title_label.grid(column=0, row=0, columnspan=2, pady=10)

        self.text_input = tk.Text(height=15, width=40, font=(FONT_NAME, 12),bg='black',fg='white')
        self.text_input.grid(column=0, row=1, columnspan=2, pady=10)
        self.text_input.config(state='disabled')

        self.timer = None
        
        self.start_button = tk.Button(text="Start", width=15, bg=RED, fg="white", command=self.start_Writing)
        self.start_button.grid(column=0, row=3, pady=10)

        self.rule_button = tk.Button(text="Rules/About us", width=15, bg=GREEN, fg="black", command=self.rules)
        self.rule_button.grid(column=1, row=3, pady=10)

    def start_Writing(self):
        self.text_input.config(state='normal')
        self.text_input.focus()
        self.start_button.config(text='Writing...',state='disabled',bg='white')
        self.text_input.bind("<KeyRelease>", self.reset_timer)
        self.start_timer()

    def start_timer(self):
        self.timer = threading.Timer(5.0, self.delete_text)
        self.timer.start()

    def reset_timer(self, event):
        if self.timer:
            self.timer.cancel()
        self.start_timer()

    def delete_text(self):
        self.text_input.delete("1.0", tk.END)
        messagebox.showwarning("Warning", "You stopped typing! All text has been deleted.")
        self.text_input.config(state='disabled')
        self.start_button.config(text='Restart',state='normal',bg=RED)
    
    def rules(self):
        messagebox.showinfo(title="Rules/About us", message='''
        Rules:
            \t✔️ When you click on start, You can write
            \t✔️ After 5 sec of Stop Writing, Text will Disappear 
        About us:
            \t🙈 Coding By Arslan Arshad,
            \t\t🔼 A Artificial Intelligence Student
            \t\t🔼 Full Stack Web-Developer
            \t\t🔼 Pyhon Web Scraper
            \t\t🔼 Python Automation

        Coming Soon..
            \t👀 Project Update with classes
            \t👀 New More Projects on GitHub
            \t👀 Stay Connected.......😊
        ''')


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
