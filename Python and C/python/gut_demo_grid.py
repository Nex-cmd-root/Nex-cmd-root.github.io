import tkinter as tk

def handle_submit():
    name = name_entry.get()
    id = id_entry.get()
    grade = grade_entry.get()

    print(name)
    print(id)
    print(grade)

    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Grid Layout System")
root.geometry("400x200")

name_label = tk.Label(root, text="Student Name:", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=10, pady=10)

id_label = tk.Label(root, text="Student ID:", font=("Arial", 12))
id_label.grid(row=1, column=0, padx=10, pady=10)

id_entry = tk.Entry(root, font=("Arial", 12))
id_entry.grid(row=1, column=1, padx=10, pady=10)

grade_label = tk.Label(root, text="Final Grade:", font=("Arial", 12))
grade_label.grid(row=2, column=0, padx=10, pady=10)

grade_entry = tk.Entry(root, font=("Arial", 12))
grade_entry.grid(row=2, column=1, padx=10, pady=10)

submit_btn = tk.Button(root, text="Submit Data", command=handle_submit, font=("Arial", 12))
submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

root.mainloop()