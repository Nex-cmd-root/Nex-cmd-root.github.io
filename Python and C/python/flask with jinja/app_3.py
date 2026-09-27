import os
import csv
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

DB_FILE = "classroom_db.csv"

def load_student_database():
    student_list = []
    if not os.path.exists(DB_FILE):
        return student_list
    with open(DB_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_list.append(row)
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
        
        with open(DB_FILE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Student ID", "Student Name", "Final Grade"])
            writer.writerow([student_id, student_name, student_grade])
            
        success_text = f"[Success] Spreadsheet updated! Registered {student_name}."
        current_roster = load_student_database()
        return render_template("form.html", alert_msg=success_text, student_list=current_roster)

    # PATH B: Modified GET view path to intercept query string lookups!
    # request.args.get() reads variables appended to the URL (e.g. ?search_query=12345)
    search_query = request.args.get("search_query", "").strip()
    full_roster = load_student_database()

    if search_query:
        # ADVANCED PYTHONIC FILTER: Keep rows only if the target text matches name or ID
        # '.lower()' checks make the search box case-insensitive!
        filtered_roster = [
            student for student in full_roster
            if search_query.lower() in student["Student Name"].lower() or search_query in student["Student ID"]
        ]
        return render_template("form.html", alert_msg=f"Showing matches for: '{search_query}'", student_list=filtered_roster)

    # If the search field was empty, display the complete database normally
    return render_template("form.html", alert_msg=None, student_list=full_roster)

if __name__ == "__main__":
    app.run(debug=True, port=5000)