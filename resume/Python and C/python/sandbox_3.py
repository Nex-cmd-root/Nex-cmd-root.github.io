# Function to add students to the student record
def add_student(database_array):
    print("-- Adding new student --\n")
    # Checking for invalid input and ensuring all fields are populated
    # Included while loop to ensure users can try again after entering erroneous input. For convenience
    while True:
        try:
            student_id = int(input("Student ID: "))
            name = input("Student name: ")
            if not name.replace(" ", "").isalpha():
                raise ValueError
            program = input("Student study stream: ")
            mark = float(input("Overall course mark (1-100): "))
            if not (1 <= mark <= 100):
                raise ValueError
            # newline purely for aesthetic enhancement
            print("\n")
            break
        except ValueError:
            print("Invalid input entered.\n")

    # the extend method here is used to add the student to the record
    database_array.extend([student_id, name, program, mark])
    print(f"-- Successfully added {name} to the database --\n")

    return



# Function to handle displaying student information
def view_students(database_array):

    # check if the student record has any data
    if not database_array:
        print("The student record is currently empty\n")
        return

    # print the data using a clean string formatting loop
    for i in range(0, len(database_array), 4):
        print(f"Student ID: {database_array[i]}\n"
              f"Student Name: {database_array[i+1]}\n"
              f"Student Program: {database_array[i+2]}\n"
              f"Overall Mark: {database_array[i+3]}\n")
    return



def update_student(database_array):

    # Ask the user for the target ID
    while True:
        try:
            id = int(input("Enter the student ID for the record you want to update."))
            print("\n")
            break
        except ValueError:
            print("Please enter a valid numerical user ID\n")

    # Check if the id is in the database_array
    if id in database_array:
        i = database_array.index(id)
        print(f"{id} has been found for student {database_array[(i + 1)]}, what would you like to do:\n")
    else:
        print("Selected id is not in the list")
        return

    # give the user options on what to do
    print("1. Modify Name,\n 2. Change program,\n 3. Edit overall mark\n\n")
    while True:
        try:
            choice = int(input("Your choice: "))
            print("\n")
            break
        except ValueError:
            print("Please Enter a valid choice (1, 2, 3).\n")

    # use a match block to determine what choice the user selected and proceed accordingly
    match choice:
        case 1:
            while True:
                try:
                    database_array[(i + 1)] = (input("Enter new name:"))
                    if not database_array[(i + 1)].replace(" ", "").isalpha():
                        raise ValueError
                    print("\n")
                    break
                except ValueError:
                    print("please enter a valid name.\n")
        case 2:
                database_array[(i + 2)] = input("Enter the new program:")
        case 3:
            while True:
                try:
                    database_array[(i + 3)] = int(input("Enter the new overall mark:"))
                    print("\n")
                    break
                except ValueError:
                    print("Please enter a valid mark from 1 to 100.\n")

    return



def delete_student(database_array):
    # Ask the user for the target ID
    while True:
        try:
            id = int(input("Enter the student ID for the record you want to delete."))
            print("\n")
            break
        except ValueError:
            print("Please enter a valid numerical user ID\n")

    # Check if the id is in the database_array
    if id in database_array:
        i = database_array.index(id)
        print(f"{id} has been found for student {database_array[(i + 1)]}.\n")
    else:
        print(f"{id} is not saved in the student record.")
        return

    # Ask the user if they are sure about deleting the record just in case
    while True:
        choice = input(f"Are you sure you want to delete {database_array[(i + 1)]}'s record y/n?")
        if choice == "y":
            del database_array[i:(i + 4)]
            print("\n")
            return
        elif choice == "n":
            print("\n")
            return
        else:                                           # handle erroneous input
            print("unrecognized input, enter y or n.\n")



def search_student(database_array):
    query = input("Enter student name or ID: ")
    
    # Use a shorthand if statement to check if the user entered a name or an id
    target = int(query) if query.isdigit() else query

    # In case the target student is not in the database
    if target not in database_array:
        print(f"{query} not found in student record.\n")
        return

    # find the index of the specific id or name so it can be used to navigate to all other entries
    i = database_array.index(target)
    
    # Adjust index if matched by name instead of ID
    if isinstance(target, str):
        i = i - 1

    print(f"Student ID: {database_array[i]}\n"
          f"Student Name: {database_array[i+1]}\n"
          f"Student Program: {database_array[i+2]}\n"
          f"Overall Mark: {database_array[i+3]}\n")
    
    return



def sort_students(database_array):
    # Initial sort options
    print("SORT OPTIONS\n\n")
    print("1. Sort by Student Name\n")
    print("2. Sort by Mark (Highest to Lowest)\n")
    print("3. Sort by Student ID\n\n")
    while True:
        try:
            choice = int(input("Enter choice"))
            print("\n")
            break
        except ValueError:
            print("Please enter a valid choice from 1 - 3\n")

    #Logic for each of the options
    match choice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass



def display_statistics(database_array):
    if not database_array:
        return

    # print number of students, highest mark, lowest mark and average mark.



def main():

    student_record = []

    # Initial option view when the terminal is opened.
    while True:
        print("STUDENT COURSE MANAGEMENT SYSTEM\n")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Sort Students")
        print("7. Display Statistics")
        print("8. Exit\n")
        # Implement a while loop inside the main loop to make it more convenient in case of Wrong input
        while True:
            try:
                choice = int(input("Enter your choice:"))
                print("\n")
                break
            except ValueError:
                print("Please enter a valid choice from 1 - 8.\n")

        # A list of checks to determine which function to use based on user input
        match choice:
            case 1:
                add_student(student_record)
            case 2:
                view_students(student_record)
            case 3:
                update_student(student_record)
            case 4:
                delete_student(student_record)
            case 5:
                search_student(student_record)
            case 6:
                pass # Yet to implement logic
            case 7:
                pass # Yet to implement logic
            case 8:
                print("--- Exiting System ---")
                break


if __name__ == "__main__":
    main()