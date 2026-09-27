class Student:
    def __init__(self, student_id, grade, name):
        self.id = student_id
        self.grade = grade
        self.name = name

def save_database(database_list):
    with open("classroom_db.txt", "w") as file:
        for i, student in enumerate(database_list, start=1):
            file.write(f"Student {i}:\n")
            file.write(f"Student ID: {student.id}\n")
            file.write(f"Student Grade: {student.grade}\n")
            file.write(f"Student Name: {student.name}\n\n")
            
    print("\nDatabase successfully saved to 'classroom_db.txt'.")

def search_student(database_list, target_id):
    for student in database_list:
        if student.id == target_id:
            # Combined into one highly descriptive print statement
            print(f"-> Target Found! Name: {student.name}, Grade: {student.grade}")
            return
    print("-> Student not found in the database.")

def main():
    database_array = []

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
            
        name = input("Enter student name: ")
        new_student = Student(student_id, grade, name)
        database_array.append(new_student)

    # 1. Save data permanently
    save_database(database_array)

    # 2. Dynamic Search: Prompt the user for an ID on the fly
    try:
        search_id = int(input("\nEnter a student ID to search for: "))
        search_student(database_array, search_id)
    except ValueError:
        print("Invalid ID format entered.")

if __name__ == "__main__":
    main()