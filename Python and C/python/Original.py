import tkinter as tk
from tkinter import messagebox

def add_exercise():
    exercise = exercise_entry.get()
    one_rep_max = exercise_entry_2.get()
    global count
    count = 1

    format = f"Exercise: {exercise}, current progression 2\nExercise count: {one_rep_max}\n\n"

    with open("Workout_routine", "a") as file:
        if exercise in file:
            messagebox.showerror("The exercise is already saved")
        else:
            file.write(f" === Exercise {count} === ")
            file.write(format)

def increment():
    try:
        with open("Workout_routine", "r") as file:
            content = file.read()

        with open("Workout_routine", "w") as file:
            for i, line in enumerate(content, start=1):
                if "Exercise count:" in line:
                    exercise_count_current = int(line.split(":")[1].strip())
                    exercise_count_temp[i] = exercise_count_current

            for i in exercise_count_temp:
                modified_content = content.replace(f"Exercise count: {exercise_count_temp[i]}", f"Exercise count: {exercise_count_temp[i] + 2}")
                file.write(modified_content)

    except Exception as e:
        messagebox.showerror("something went wrong, does the file \"Workout_routine\" exist?")

def review_progression():
    messagebox.showinfo("Status", f"Your currently doing {count} exercises")
    # maybe add a way to change the increment function or adjust it

root = tk.Tk()
root.title("Exercise Tracker")
root.geometry("800x550")

exercise_label = tk.Label(root, text="Enter your exercise below.", font=("Arial", 24))
exercise_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

exercise_entry = tk.Entry(root, font=("Arial", 12))
exercise_entry.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

exercise_label_2 = tk.Label(root, text="Current one rep max:", font=("Arial", 16))
exercise_label_2.grid(row=2, column=0, pady=10, padx=10)
exercise_entry_2 = tk.Entry(root, font=("Arial", 12))
exercise_entry_2.grid(row=2, column=1, pady=10, padx=10)

exercise_btn = tk.Button(root, text="Add to exercise list", command=add_exercise, font=("Arial", 12))
exercise_btn.grid(row=3, column=0, pady=10, padx=10)
exercise_btn_2 = tk.Button(root, text="Adjust progression", command=review_progression, font=("Arial", 12))
exercise_btn_2.grid(row=3, column=2, pady=10, padx=10)

exercise_btn_3 = tk.Button(root, text="Push your one rep max.", command=increment, font=("Arial", 12))
exercise_btn_3.grid(row=4, column=2, pady=10, padx=10)

root.mainloop()