import tkinter as tk

# 1. Define the action (Function) that happens when the button is clicked
def handle_button_click():
    # Update the text of our label widget dynamically
    status_label.config(text="Hello, World! You clicked the button!")

# 2. Create the main application window
root = tk.Tk()
root.title("My First Python GUI")
root.geometry("400x200")  # Sets the window size (Width x Height in pixels)

# 3. Create a text label widget
# We tell it to live inside 'root', and set its initial text
status_label = tk.Label(root, text="Welcome! Click the button below.", font=("Arial", 14))
status_label.pack(pady=20)  # 'pack' draws it on screen. 'pady' adds vertical space.

# 4. Create a clickable button widget
# The 'command' parameter links the button directly to our function above
click_button = tk.Button(root, text="Click Me", command=handle_button_click, font=("Arial", 12))
click_button.pack(pady=10)

# 5. Start the Event Loop
# This keeps the window open and active on your desktop screen
root.mainloop()