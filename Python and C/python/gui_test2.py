import tkinter as tk

root = tk.Tk()
root.title("My First Python GUI")
root.geometry("600x400")

#text widget for user input.
name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

#Extract user input from the widget.
def handle_button_click():
    User_name = name_entry.get()
    status_label.config(text=f"Hello, {User_name}! You clicked the button.")

status_label = tk.Label(root, text="Enter your name above then click the button below.", font=("Arial", 14))
status_label.pack(pady=20)

click_button = tk.Button(root, text="Click me", command=handle_button_click, font=("Arial", 12))
click_button.pack(pady=10)

root.mainloop()