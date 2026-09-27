import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, student_id, grade, name):
        self.id = student_id
        self.grade = grade
        self.name = name

def handle_submit():
    name = name_entry.get()
    raw_id = id_entry.get()
    raw_grade = grade_entry.get()

    if not name or not raw_id or not raw_grade:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        student_id = int(raw_id)
        grade = int(raw_grade)
    except ValueError:
        messagebox.showerror("Error", "ID and Grade must be numbers!")
        return

    new_student = Student(student_id, grade, name)

    with open("classroom_db.txt", "a") as file:
        file.write(f"Student ID: {new_student.id}\n")
        file.write(f"Student Grade: {new_student.grade}\n")
        file.write(f"Student Name: {new_student.name}\n")
        file.write("-" * 30 + "\n") # Visual divider in the text file

    messagebox.showinfo("Success", f"Successfully saved record for {name}!")

    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)

def handle_search():
    id = search_entry.get()

    # Safety Validation: Ensure the ID field is not empty
    if not id:
        messagebox.showerror("Error", "ID field is required!")
        return

    # Data Type Integrity: Enforce digit safety just like try/except in handle_submit()
    try:
        id = int(id)
    except ValueError:
        messagebox.showerror("Error", "ID must be a number!")
        search_entry.delete(0, tk.END) # Clear the search entry field for user convenience
        return

    id = str(id) # Convert the ID to string for comparison with the text file content

    # Search Logic: Check if the ID exists in the database file
    with open("classroom_db.txt", "r") as file:
        for line in file: # Iterate through each line in the file
            if line.strip() == f"Student ID: {id}": # Check if the line matches the ID format
                messagebox.showinfo("Search Result", f"{id} is saved in the database")
                break
        else: # This else corresponds to the for loop, not the if statement. It executes if the loop completes without a break.
            messagebox.showinfo("Search Result", f"{id} is not saved in the database")


root = tk.Tk()
root.title("Student Database Interface")
root.geometry("760x440")

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

search_label = tk.Label(root, text="Search ID:", font=("Arial", 12))
search_label.grid(row=4, column=0, padx=10, pady=10)
search_entry = tk.Entry(root, font=("Arial", 12))
search_entry.grid(row=4, column=1, padx=10, pady=10)
search_btn = tk.Button(root, text="Search", command=handle_search, font=("Arial", 12))
search_btn.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()