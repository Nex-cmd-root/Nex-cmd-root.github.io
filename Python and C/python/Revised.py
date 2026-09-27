import json
import os
import tkinter as tk
from tkinter import messagebox, ttk

# --- FILE HANDLERS ---
DATA_FILE = "workouts.json"


def load_data():
    """Reads workout data from JSON file. Returns empty dict if file missing/corrupt."""
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def save_data(data):
    """Saves the current dictionary to the JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# --- APPLICATION FUNCTIONS ---
def update_display():
    """Refreshes the Listbox with the latest data from workouts dict."""
    exercise_listbox.delete(0, tk.END)
    for name, stats in workouts.items():
        display_str = f"{name}  |  1RM: {stats['one_rep_max']} kg  |  Progression step: +{stats['increment']}"
        exercise_listbox.insert(tk.END, display_str)


def add_exercise():
    name = entry_name.get().strip().title()
    max_val = entry_max.get().strip()

    # Validation: Check for empty fields
    if not name or not max_val:
        messagebox.showwarning("Missing Input", "Please fill in all fields.")
        return

    # Validation: Ensure 1RM is a positive number
    try:
        max_val = float(max_val)
        if max_val <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Input", "One Rep Max must be a positive number."
        )
        return

    # Store in our in-memory dictionary
    workouts[name] = {"one_rep_max": max_val, "increment": 2.5}

    save_data(workouts)
    update_display()

    # Clear entry fields
    entry_name.delete(0, tk.END)
    entry_max.delete(0, tk.END)
    messagebox.showinfo("Success", f"Added/Updated '{name}'!")


def increment_selected():
    """Increments the One Rep Max for the item selected in the Listbox."""
    try:
        selected_index = exercise_listbox.curselection()[0]
        selected_text = exercise_listbox.get(selected_index)

        # Extract the exercise name from the display text
        exercise_name = selected_text.split("  |")[0]

        # Update numerical value
        step = workouts[exercise_name]["increment"]
        workouts[exercise_name]["one_rep_max"] += step

        save_data(workouts)
        update_display()

    except IndexError:
        messagebox.showwarning(
            "Selection Error", "Please select an exercise from the list first."
        )


def delete_selected():
    """Removes selected exercise from storage."""
    try:
        selected_index = exercise_listbox.curselection()[0]
        selected_text = exercise_listbox.get(selected_index)
        exercise_name = selected_text.split("  |")[0]

        del workouts[exercise_name]
        save_data(workouts)
        update_display()

    except IndexError:
        messagebox.showwarning(
            "Selection Error", "Select an exercise to delete."
        )


# --- UI SETUP ---
root = tk.Tk()
root.title("Workout Progression Tracker")
root.geometry("600x520")
root.configure(bg="#f4f4f9")

# Load existing data on startup
workouts = load_data()

# Styling Header
header = tk.Label(
    root,
    text="Exercise Progression Tracker",
    font=("Helvetica", 18, "bold"),
    bg="#f4f4f9",
    fg="#333333",
)
header.pack(pady=15)

# Entry Frame (Grouping inputs together)
input_frame = tk.Frame(root, bg="#f4f4f9")
input_frame.pack(pady=10)

tk.Label(
    input_frame, text="Exercise Name:", font=("Arial", 11), bg="#f4f4f9"
).grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_name = tk.Entry(input_frame, font=("Arial", 11), width=20)
entry_name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(
    input_frame,
    text="Current 1RM (kg/lbs):",
    font=("Arial", 11),
    bg="#f4f4f9",
).grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_max = tk.Entry(input_frame, font=("Arial", 11), width=20)
entry_max.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(
    input_frame,
    text="Add / Update Exercise",
    command=add_exercise,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

# Display Area (Listbox with Scrollbar)
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill="both", expand=True, padx=20)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

exercise_listbox = tk.Listbox(
    list_frame,
    font=("Consolas", 11),
    yscrollcommand=scrollbar.set,
    selectbackground="#007ACC",
)
exercise_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=exercise_listbox.yview)

# Action Buttons Frame
action_frame = tk.Frame(root, bg="#f4f4f9")
action_frame.pack(pady=15)

btn_increment = tk.Button(
    action_frame,
    text="💪 Push 1RM (+2.5)",
    command=increment_selected,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
)
btn_increment.pack(side="left", padx=10)

btn_delete = tk.Button(
    action_frame,
    text="🗑️ Delete Selected",
    command=delete_selected,
    bg="#f44336",
    fg="white",
    font=("Arial", 11),
    padx=10,
)
btn_delete.pack(side="left", padx=10)

# Populate window on launch
update_display()

root.mainloop()