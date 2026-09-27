# 1. IMPORT THE WEB ENGINE
from flask import Flask

# Initialize our Flask application factory box
app = Flask(__name__)

# 2. DEFINE THE LANDING PAGE ROUTE
# This tells Python: "When a browser requests the main page '/', run this function"
@app.route("/")
def home_page():
    # We return raw HTML text strings that Google Chrome can render visually
    return """
    <html>
        <head>
            <title>My Python Web Server</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding-top: 50px; background-color: #f4f4f9; }
                h1 { color: #333366; }
                p { color: #666; font-size: 18px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Your First Python Web App!</h1>
            <p>This page is being served live out of your computer's RAM using Flask backend routing.</p>
            <hr width='50%'>
            <p style='color: green; font-weight: bold;'>Status: Active and Connected</p>
        </body>
    </html>
    """

# 3. RUN THE LOCAL WEB SERVER
if __name__ == "__main__":
    # 'debug=True' means the server will automatically refresh if you change your code
    print("\n--- Starting Local Web Server Engine ---")
    print("Open your browser and navigate to: http://127.0.0.1:5000/")
    app.run(debug=True)