import tkinter as tk
from tkinter import messagebox  # Built-in visual popup alerts tool

# 1. THE STUDENT CLASS
class Student:
    def __init__(self, student_id, grade, name):
        self.id = student_id
        self.grade = grade
        self.name = name

# 2. THE BACKEND SUBMISSION LOGIC
def handle_submit():
    name = name_entry.get()
    raw_id = id_entry.get()
    raw_grade = grade_entry.get()

    # Safety Validation: Ensure columns are not empty
    if not name or not raw_id or not raw_grade:
        messagebox.showerror("Error", "All fields are required!")
        return

    # Data Type Integrity: Enforce digit safety just like try/except in main()
    try:
        student_id = int(raw_id)
        grade = int(raw_grade)
    except ValueError:
        messagebox.showerror("Error", "ID and Grade must be numbers!")
        return

    # Create our structural data instance object
    new_student = Student(student_id, grade, name)

    # APPEND MODE: Instantly record this single student package to disk
    with open("classroom_db.txt", "a") as file:
        file.write(f"Student ID: {new_student.id}\n")
        file.write(f"Student Grade: {new_student.grade}\n")
        file.write(f"Student Name: {new_student.name}\n")
        file.write("-" * 30 + "\n") # Visual divider in the text file

    # Visual user confirmation popup
    messagebox.showinfo("Success", f"Successfully saved record for {name}!")

    # UX Polish: Wipe text frames so the user can input the next record effortlessly
    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)


# 3. THE DESKTOP DESIGN INTERFACE
root = tk.Tk()
root.title("Student Database Interface")
root.geometry("380x220")

# Layout Rows
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