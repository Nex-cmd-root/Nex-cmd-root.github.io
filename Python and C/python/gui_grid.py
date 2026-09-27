import tkinter as tk

def handle_submit():
    # We will hook up database logic here later
    pass

root = tk.Tk()
root.title("Grid Layout System")
root.geometry("400x200")

# --- ROW 0: Name Label and Entry ---
# 'padx' adds padding to the left and right of the widget
name_label = tk.Label(root, text="Student Name:", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

# --- ROW 1: Grade Label and Entry ---
grade_label = tk.Label(root, text="Final Grade:", font=("Arial", 12))
grade_label.grid(row=1, column=0, padx=10, pady=10)

grade_entry = tk.Entry(root, font=("Arial", 12))
grade_entry.grid(row=1, column=1, padx=10, pady=10)

# --- ROW 2: Submit Button ---
# 'columnspan=2' stretches the button across both columns so it looks centered
submit_btn = tk.Button(root, text="Submit Data", command=handle_submit, font=("Arial", 12))
submit_btn.grid(row=2, column=0, columnspan=2, pady=15)

root.mainloop()