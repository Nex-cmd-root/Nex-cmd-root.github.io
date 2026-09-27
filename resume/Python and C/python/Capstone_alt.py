# =====================================================================
# 1. THE PACKAGE (Replaces 'struct student')
# Python uses "Classes" instead of structs. They do the exact same job,
# but they allow you to initialize values directly inside them.
# =====================================================================
class Student:
    def __init__(self, student_id, grade, name):
        self.id = student_id
        self.grade = grade
        self.name = name


# =====================================================================
# 2. THE FILE STORAGE MODULE (Replaces 'void save_database')
# Notice we don't need pointer types (*) or return type declarations.
# =====================================================================
def save_database(database_list):
    # The 'with' keyword opens the file and AUTOMATICALLY closes it 
    # when the indented block finishes. No 'fclose()' required!
    with open("classroom_db.txt", "w") as file:
        # 'enumerate' automatically tracks the loop index (i) and the item
        for i, student in enumerate(database_list, start=1):
            file.write(f"Student {i}:\n")
            file.write(f"Student ID: {student.id}\n")
            file.write(f"Student Grade: {student.grade}\n")
            file.write(f"Student Name: {student.name}\n\n")
            
    print("\nDatabase successfully saved to 'classroom_db.txt'.")


# =====================================================================
# 3. THE CORE EXECUTION (Replaces 'int main')
# Python runs from top to bottom. We don't need an explicit main function,
# but we can simulate one.
# =====================================================================
def main():
    # Python Lists are dynamic arrays. They resize automatically!
    # No 'malloc', no 'sizeof', and absolutely NO 'free()'.
    database_array = []

    # Safe input checking is built-in. 'try/except' handles bad inputs
    # instead of checking scanf return values and flushing buffers with getchar.
    try:
        num_students = int(input("How many students are in your class?\n"))
    except ValueError:
        print("Invalid number. Exiting.")
        return

    for i in range(num_students):
        print(f"\nEntering data for student {i + 1}:")
        
        try:
            student_id = int(input("Enter student ID (format: xxxxx): "))
            grade = int(input("Enter student grade (0 to 100): "))
        except ValueError:
            print("Invalid digits entered. Exiting.")
            return
            
        # 'input()' reads strings seamlessly without buffer overflows or trailing newlines!
        name = input("Enter student name: ")

        # Create a new student object instance on the fly
        new_student = Student(student_id, grade, name)
        
        # '.append' throws the student into our dynamic array instantly
        database_array.append(new_student)

    # Call our saving function
    save_database(database_array)


# This tiny piece of plumbing tells Python to run main() when you click play
if __name__ == "__main__":
    main()