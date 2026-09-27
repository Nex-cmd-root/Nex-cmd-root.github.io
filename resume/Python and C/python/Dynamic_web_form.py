from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    # This automatically sends the user straight to the form
    from flask import redirect
    return redirect("/submit")

# We tell this route it is allowed to handle BOTH loading the form (GET) 
# and receiving the submitted text data (POST)
@app.route("/submit", methods=["GET", "POST"])
def submit_student():
    # PATH A: The user just clicked the Submit button! Process the incoming network data.
    if request.method == "POST":
        # Extract the data using the 'name' attribute from the HTML input tags
        student_name = request.form.get("form_name")
        student_id = request.form.get("form_id")
        student_grade = request.form.get("form_grade")
        
        # Open your database text file and log it permanently to disk
        with open("classroom_db.txt", "a", encoding="utf-8") as file:
            file.write(f"ID: {student_id} | Name: {student_name} | Grade: {student_grade}\n")
            
        # Return a success message back to the web browser screen
        return f"<h3>[Success] Web data intercepted! Saved profile for: {student_name}</h3><a href='/submit'>Back to Form</a>"

    # PATH B: The user is just visiting the page normally (GET). Send them the empty visual form template.
    return """
    <html>
        <head>
            <title>Web Database Entry Form</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9; }
                form { background: white; padding: 20px; display: inline-block; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
                input { margin: 10px; padding: 8px; width: 200px; font-size: 14px; }
                button { padding: 10px 20px; background-color: #333366; color: white; border: none; border-radius: 4px; cursor: pointer; }
            </style>
        </head>
        <body>
            <h2>Student Registry Web Portal</h2>
            <!-- action='/submit' tells the browser where to blast the data bundle when clicked -->
            <form action="/submit" method="POST">
                <input type="text" name="form_name" placeholder="Enter Student Name" required><br>
                <input type="text" name="form_id" placeholder="Enter Student ID" required><br>
                <input type="text" name="form_grade" placeholder="Enter Grade" required><br>
                <button type="submit">Register Student</button>
            </form>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5000)