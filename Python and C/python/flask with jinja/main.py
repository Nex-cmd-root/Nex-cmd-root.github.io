from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/submit")

@app.route("/submit", methods=["GET", "POST"])
def submit_student():
    # PATH A: The user clicked register! Process the data bundle
    if request.method == "POST":
        student_name = request.form.get("form_name")
        student_id = request.form.get("form_id")
        student_grade = request.form.get("form_grade")
        
        with open("classroom_db.txt", "a", encoding="utf-8") as file:
            file.write(f"ID: {student_id} | Name: {student_name} | Grade: {student_grade}\n")
            
        # Formulate a clean validation text string
        success_text = f"[Success] Intercepted record for {student_name}!"
        
        # Reload the HTML template page, passing our success text down the Jinja line!
        try:
            with open("classroom_db.txt", "r", encoding="utf-8") as file:
                students_raw = file.readlines()
        except FileNotFoundError:
                students_raw = []
        return render_template("form.html", alert_msg=success_text, student_list=students_raw)

    # PATH B: Regular page view. Render our visual template cleanly with no alert message
    try:
        with open("classroom_db.txt", "r", encoding="utf-8") as file:
            students_raw = file.readlines()
    except FileNotFoundError:
        students_raw = []
    return render_template("form.html", alert_msg=None, student_list=students_raw)

if __name__ == "__main__":
    app.run(debug=True, port=5000)