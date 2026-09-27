import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Student:
    def __init__(self, student_id, grade, name):
        self.id = student_id
        self.grade = grade
        self.name = name

    def get_letter_grade(self):
            if self.grade >= 90:
                return "A+"
            elif self.grade >= 80:
                return "A"
            elif self.grade >= 70:
                return "B"
            else:
                return "Passing"
    
    def format_for_file(self):
        return (
            f"Student ID: {self.id}\n"
            f"Student Grade: {self.grade} ({self.get_letter_grade()})\n"
            f"Student Name: {self.name}\n"
            f"{'-' * 30}\n"
        )

    @classmethod
    def load_from_file(cls, filename):
        student_list = []
        try:
            with open(filename, "r") as file:
                current_id = None
                current_grade = None
                
                for line in file:
                    if "Student ID:" in line:
                        current_id = int(line.split(":")[1].strip())
                    elif "Student Grade:" in line:
                        # Grab just the numeric digits before the space and parenthesis
                        current_grade = int(line.split(":")[1].split()[0].strip())
                    elif "Student Name:" in line:
                        current_name = line.split(":")[1].strip()
                        
                        # Once we have gathered all 3 fields, assemble the object!
                        # 'cls' acts exactly like calling 'Student(current_id, ...)'
                        new_student = cls(current_id, current_grade, current_name)
                        student_list.append(new_student)
                        
        except FileNotFoundError:
            pass # Return an empty list if file doesn't exist yet
            
        return student_list

    def parse_database_and_plot():
        # Let the Student factory do all the dirty parsing work!
        students = Student.load_from_file("classroom_db.txt")
    
        if not students:
            messagebox.showinfo("Info", "No student data available.")
            return

        # Use a quick Python list comprehension to extract values
        names = [s.name for s in students]
        grades = [s.grade for s in students]

        plt.figure(figsize=(10, 5)) # Sets width and height dimensions of the popup window
    
        # Draw a bar chart (X axis = Names, Y axis = Grades)
        plt.bar(names, grades, color="skyblue", edgecolor="black")
    
        # Add descriptive chart labels
        plt.title("Classroom Grade Performance", fontsize=16, fontweight="bold")
        plt.xlabel("Student Names", fontsize=12)
        plt.ylabel("Grades (0-100)", fontsize=12)
        plt.ylim(0, 100)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        plt.show()

    def handle_search():
        students = Student.load_from_file("classroom_db.txt")

        target_id = int(search_entry.get())
        id = [s.id for s in students]

        if target_id in id:
            messagebox.showinfo("Search Result", f"{target_id} is saved in the database")
        else:
            messagebox.showinfo("Search Result", f"{target_id} is not saved in the database")

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
        file.write(new_student.format_for_file())

    messagebox.showinfo("Success", f"{name}'s record has been recorded with an overall score of {new_student.get_letter_grade()}")

    name_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)



root = tk.Tk()
root.title("Student Database Interface")
root.geometry("760x440")

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
search_btn = tk.Button(root, text="Search", command=Student.handle_search, font=("Arial", 12))
search_btn.grid(row=4, column=2, padx=10, pady=10)

chart_btn = tk.Button(root, text="Visualize Grades", command=Student.parse_database_and_plot, font=("Arial", 12))
chart_btn.grid(row=5, column=0, columnspan=2, pady=15)

root.mainloop()