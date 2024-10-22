import os
import tkinter as tk
from tkinter import scrolledtext

def run_command():
    command = command_entry.get()
    output = os.popen(command).read()
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output)

app = tk.Tk()
app.title("Linux Terminal Connector")

command_entry = tk.Entry(app, width=50)
command_entry.pack(pady=10)

run_button = tk.Button(app, text="Run Command", command=run_command)
run_button.pack(pady=5)

output_text = scrolledtext.ScrolledText(app, width=60, height=20)
output_text.pack(pady=10)

app.mainloop()
