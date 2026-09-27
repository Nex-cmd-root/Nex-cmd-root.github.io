import matplotlib.pyplot as plt

def parse_database_and_plot():
    names = []
    grades = []
    
    # 1. Read the text file and parse out the data fields
    try:
        with open("classroom_db.txt", "r") as file:
            for line in file:
                if "Student Grade:" in line:
                    # Split at the colon, grab the second half, remove spaces, make it an int
                    grade_val = int(line.split(":")[1].strip())
                    grades.append(grade_val)
                elif "Student Name:" in line:
                    name_val = line.split(":")[1].strip()
                    names.append(name_val)
    except FileNotFoundError:
        print("Database file not found yet! Add some students first.")
        return

    # Check if we have data to plot
    if not names:
        print("No student data available to visualize.")
        return

    # 2. Build the graph layout using Matplotlib
    plt.figure(figsize=(10, 5)) # Sets width and height dimensions of the popup window
    
    # Draw a bar chart (X axis = Names, Y axis = Grades)
    plt.bar(names, grades, color="skyblue", edgecolor="black")
    
    # Add descriptive chart labels
    plt.title("Classroom Grade Performance", fontsize=16, fontweight="bold")
    plt.xlabel("Student Names", fontsize=12)
    plt.ylabel("Grades (0-100)", fontsize=12)
    plt.ylim(0, 100) # Lock the Y-axis boundary limit from 0 to 100
    plt.grid(axis='y', linestyle='--', alpha=0.7) # Add subtle background lines

    # 3. Render the interactive window frame on your desktop screen
    plt.show()

# Run the test plotting function manually
if __name__ == "__main__":
    parse_database_and_plot()