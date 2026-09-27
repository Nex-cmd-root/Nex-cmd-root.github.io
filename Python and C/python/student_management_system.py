# Student Course Management System
# CIT102 - Assignment 1 (S2 2026)


def  display_menu():
    """displays the main menu options."""
    print("/n" + "=" * 36)
    print("1. add student")
    print("2. view all students")
    print("3. update student")
    print("4. delete student")
    print("5. search student")
    print("6. sort students")
    print("7. display statistics")
    print("8. exit")
    print("=" * 36)

def add_student(students):
    """adds a new student record to the list."""
    print("/n--- ADD NEW STUDENT ---")

    # Iput and check for duplicate student ID
    while True:
        student_id = input("enter student ID: ").strip()
        if not student_id:
            print("student ID cannot be empty.")
            continue
        # check if ID already exists
        exists = any(std["id"].lower() == student_id.lower()for std in students)
        if exists:
            print(f"error: a student with ID '{student_id}' already exists.")
        else:
            break

    name = input("enter student name: ").strip()
    while not name:
        print("name cannot be empty.")
        name = input("enter student name: ").strip()

    programme = input("enter programme: ").strip()
    while not programme:
        print("programme cannot be empty.")
        programme = input("enter programme: ").strip()

    # Input validation for course mark
    while True:
        try:
            mark = float(input("entet course mark (0-100): "))
            if 0<= mark <= 100:
                break
            else:
                print("error: mark must be between 0 and 100.")
        except ValueError:
            print("Invalid input please entet a numerical value for the mark.")

    #Creat record and add to list
    student_record = {
        "id": student_id,
        "name": name,
        "programme": programme,
        "mark": mark
    }                
    students.append(student_record)
    print(f"/nsuccess: student '{name}' added successfully!")

def view_all_students(students):
    """display all student records in a format table."""
    print("/n--- ALL STUDENT RECORDS ---")
    if not students:
        print("no student records found.")


    # print formatted headers 
    print("-" * 65)
    print(f"{'ID':>12} ,{'name':<20} ,{'programme':<15} {'mark':<8} ") 
    print("-"* 65)
    for std in students:
        print(f"{std['id']:>12} {std['name']:<20} {std['programme']:<15} {std['mark']:<8.2f}")
    print("-"* 65)

def update_student(students):
    """Updates an existing student`s details."""
    print("/n--- UPDATE STUDENT ---")
    if not students:
        print("no records available to update.")
        return

    student_id = input("Enter Student ID to update: ").strip()
    student = next((std for std in students if std['id'].lower() == student_id.lower()))

    if not student:
        print(f"Error: No student found with ID '{student_id}'.")
        return

    print(f"/nUpdating detials for {student['name']} (Leave blank to keep current value)")

    #Update Name
    new_name = input(f"New Name [{student['name']}]: ").strip()
    if new_name:
        student['name'] = new_name

    #Update Programme
    new_programme = input(f"New Programme [{student['programme']}]:").strip()
    if new_programme:
        student['programme'] = new_programme

    # Update Mark
    new_mark_str = input(f"New Mark [{student['mark']}]: ").strip()
    if new_mark_str:
        while True:
            try:
                new_mark = float(new_mark_str)
                if 0 <= new_mark <= 100:
                    student['mark'] = new_mark
                    break
                else:
                    print("Error: Mark must be between 0 100.")
            except ValueError:
                print("Invalid numerical input.")
            new_mark_str = input("Re-enter New Mark: ").strip()


    print("/nSuccess: Student details updated successfully!")



def delete_student(students):
    """Deletes a student record by ID."""
    print("/n--- DELETE STUDENT ---")
    if not students:
        print("No records available to delete.")
        return

    student_id = input("Enter Student ID to delete: ").strip()
    student = next((std for std in students if std['id'].lower() == student_id.lower()), None)

    if not student:
        print(f"Error: No student found with ID '{student_id}'.")
        return

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete '{student['name']}'? (y/n): ").strip().lower()
    if confirm == 'y':
        students.remove(student)
        print("Success: Student record deleted.")

    else:
        print("Action cancelled.")


def search_student(students):
    """Searches for a student by ID or Name."""
    print("\n--- SEARCH STUDENT ---")
    if not students:
        print("No student records available")
        return

    term = input("Enter Student ID or Name to search: ").strip().lower()
    results = [
        std for std in students 
        if term in std['id'].lower() or term in std['name'].lower() 
    ]                                    

    if not results:
        print(f"No student matching '{term}' was found.")
    else:
        print(f"/nFound {len(results)} matching records(s):")    
        view_all_students(results)


def  sort_student(students):
    """ Sorts student records based on user preference."""
    print("/n--- SORT STUDENTS ---")
    if not students:
        print("No records available to sort.")
        return

    print("Sort Options:")
    print("1. Sort by ID")
    print("2. Sort by Name")
    print("3. Sort by Mark (High to Low)")
    print("4. Sort by Mark (Low to High)")

    choice = input("Enter choice (1-4): ").strip()

    if choice == '1':
        students.sort(key=lambda x: x['id'].lower())
        print("Students sorted by ID.")
    elif choice =='2':
        students.sort(key=lambda x: x['name'].lower())
        print("Students sorted by Name.")
    elif choice =='3':
        students.sort(key=lambda x: x['mark'], reverse=True)
        print("Students sorted by Mark  (Highest to Lowest).")
    elif choice =='4':
             students.sort(key=lambda x: x['mark'])
             print("Students sorted by Mark  (Lowest to Highest).")
    else:
        print("Invalid sorting option.")
        return

    view_all_students(students)            



def display_statistics(students):
    """Displays summary analytics for student performance."""
    print("/n--- COURSE STATISTICS ---")
    if not students:
        print("No student data available to comute statistics.")
        return

    total_students = len(students)
    marks = [std['mark'] for std in students]

    avg_mark = sum(marks)  /  total_students
    highest_mark = max(marks)
    lowest_mark = min(marks)

    #Count passes (Assuming 50 is pass mark) 
    passes = sum(1 for m in marks if m >= 50)
    fails = total_students - passes 
    pass_rate = (passes / total_students) * 100

    print(f"Total Enrolled Students : {total_students}")
    print(f"Average Course Mark  : {avg_mark:.2f}")
    print(f"Highest Mark           : {highest_mark:.2f}")
    print(f"Lowest Mark         : {lowest_mark:.2f}")
    print(f"Passing Students (>= 50): {passes} ({pass_rate:.1f}%)")
    print(f"Failing Students (<50) : {fails}")



def main():
    """Main program execution loop."""
    # List storing all student dictionaries
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            search_student(students)
        elif choice == '6':
            sort_student(students)
        elif choice == '7':
            display_statistics(students)
        elif choice == '8':
            print("/nThank you for using the student Course Management System. Goodbye!")
            break
        else:
            print("/nInvalid choice! Please select a valid option (1-8).")



    if __name__ == "__main__":
        main()                            

