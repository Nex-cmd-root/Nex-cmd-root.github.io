import os
import csv
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

DB_FILE = "classroom_db.csv"

# HELPER FUNCTION: Safely reads the CSV matrix and converts it into a list of dictionaries
def load_student_database():
    student_list = []
    if not os.path.exists(DB_FILE):
        return student_list # Return empty array if file isn't created yet
        
    with open(DB_FILE, "r", encoding="utf-8") as file:
        # DictReader automatically treats the very first line of our CSV as Column Headers!
        reader = csv.DictReader(file)
        for row in reader:
            student_list.append(row) # Sweeps up data rows as clean dictionary maps
            
    return student_list

@app.route("/")
def home():
    return redirect("/submit")

@app.route("/submit", methods=["GET", "POST"])
def submit_student():
    file_exists = os.path.exists(DB_FILE)

    if request.method == "POST":
        student_name = request.form.get("form_name")
        student_id = request.form.get("form_id")
        student_grade = request.form.get("form_grade")
        
        # Open our new spreadsheet file in append mode ("a")
        # 'newline=""' is a mandatory requirement to prevent double spacing errors in Windows Excel
        with open(DB_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # If this is a brand-new file, we MUST write the Column Header row first!
            if not file_exists:
                writer.writerow(["Student ID", "Student Name", "Final Grade"])
                
            # Write our clean database column data packet array
            writer.writerow([student_id, student_name, student_grade])
            
        success_text = f"[Success] Spreadsheet updated! Registered {student_name}."
        
        # FIX: Ensure we reload the updated dataset for BOTH paths!
        current_roster = load_student_database()
        return render_template("form.html", alert_msg=success_text, student_list=current_roster)

    # PATH B: Regular GET view path load
    current_roster = load_student_database()
    return render_template("form.html", alert_msg=None, student_list=current_roster)

if __name__ == "__main__":
    app.run(debug=True, port=5000)