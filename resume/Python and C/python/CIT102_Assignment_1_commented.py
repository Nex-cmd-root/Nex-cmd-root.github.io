# Function to add students to the student record
def add_student(database_array):
    print("--- Adding new student ---\n")
    # Main loop that enters the student information and checks for errors in the input
    # Features implemented are checking for invalid input and ensuring all fields are populated
    # Included while loop to ensure users can try again after entering erroneous input. For convenience
    while True:
        try:
            student_id = int(input("Student ID: "))
            if student_id in database_array:
                print("Student ID already exists in the record, please enter a unique ID.\n")
                raise ValueError
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
    print(f"--- Successfully added {name} to the database ---\n")

    return



# Function to handle displaying student information
def view_students(database_array):

    # check if the student record has any data
    if not database_array:
        print("The student record is currently empty\n")
        return

    # A for loop to print the data using clean string formatting
    for i in range(0, len(database_array), 4):
        print(f"Student ID: {database_array[i]}\n"
              f"Student Name: {database_array[i+1]}\n"
              f"Student Program: {database_array[i+2]}\n"
              f"Overall Mark: {database_array[i+3]}\n")
    return



# A simple function to update student information, it uses the same logic as the add_student function but with
# a few modifications to allow for the user to select which field they want to update
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
        print("Selected id is not in the student record, please try again.\n")
        return

    # give the user various options detailing what they can do to update the student record
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



# A function to delete a student record from the database using the student ID as a reference point
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



# A function to search for a student record using either the student ID or the student name as a reference point
def search_student(database_array):
    query = input("Enter student name or ID: ")
    
    # a shorthand if statement to check if the user entered a name or an id
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



# A complex function to sort the student record as required in the assignment
def sort_students(database_array):
    #Initial sort options and a user input to determine which sorting method to use, includes error handling for
    #invalid input and empty student record
    print("SORT OPTIONS\n")
    print("1. Sort by Student Name")
    print("2. Sort by Mark (Highest to Lowest)")
    print("3. Sort by Student ID\n")
    while True:
        try:
            choice = int(input("Enter choice"))
            if choice < 1 or choice > 3:
                print("Invalid range please enter a number from 1 - 3\n")
                raise ValueError
            if not database_array:
                print("No students detected in the record, populate the record first.\n")
                return
            print("\n")
            break
        except ValueError:
            print("Please enter a valid choice from 1 - 3\n")

    #Logic for each of the options which basically works as their own functions but are all contained in this one function for convenience
    match choice:
        case 1:
            # Store all letters of the alphabet as a list for purposes of the sort logic to come
            alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
            alphabet_upper = [letter.upper() for letter in alphabet_lower]

            # Create empty lists that will all function as temporary containers
            temp_storage = []
            ordered_pair = []
            result = []

            # Isolate all the names from the student record and pair them with the index number so we can use the number to determine how we sort
            for i in range(1, len(database_array), 4):
                temp = database_array[i]
                if temp[0] in alphabet_upper:
                    index = alphabet_upper.index(temp[0])
                else:
                    index = alphabet_lower.index(temp[0])
                temp_storage.extend([index])
                linked = list((temp, temp_storage[i // 4]))
                ordered_pair.extend([linked])

            # Take the new list of tuples and order it like the list name actually implies
            ordered_pair.sort(key=lambda x: x[1])

            # Empty one of the lists to be used to store the new alphabetically sorted list
            temp_storage = []
            for x in range(0, len(ordered_pair)):
                temp = ordered_pair[x][0]
                temp_storage.extend([temp])

            # Note: current logic could use some polishing as it only sorts using the first word and could
            # place something like Alex before Aaron
            for x in temp_storage:
                index = database_array.index(x)
                result.extend([database_array[index - 1], database_array[index], database_array[index + 1], database_array[index + 2]])

            database_array[:] = result

            print("--- Successfully sorted all students ---")

        case 2:
            storage = []
            temp = []

            # Extract all the marks from the database
            for x in range(3, len(database_array), 4):
                temp.extend([database_array[x]])

            # Sort the marks from highest to lowest and use the sorted list to determine the order of the new student record
            temp.sort(reverse = True)
            for x in temp:
                index = database_array.index(x)
                storage.extend([database_array[index - 3], database_array[index - 2], database_array[index - 1], database_array[index],])

            # Assign the sorted list to the student record
            database_array[:] = storage

            print("--- successfully sorted all students ---")

        case 3:
            storage = []
            temp = []

            # Extract all the ID's from the record
            for x in range(0, len(database_array), 4):
                temp.extend([database_array[x]])

            # Sort the ID's from lowest to highest similar to student ID's at Northrise where smaller values
            # are generally used to represent senior students
            # use the sorted list to determine the order of the new student record
            temp.sort()
            for x in temp:
                index = database_array.index(x)
                storage.extend([database_array[index], database_array[index + 1], database_array[index + 2], database_array[index + 3],])

            # Assign the sorted list to the student record
            database_array[:] = storage

            print("--- successfully sorted all students ---")

    return



# A function to display statistics about the student record, it uses a for loop to isolate the marks
# and then uses the max and min functions to determine the highest and lowest mark respectively
def display_statistics(database_array):
    # check if the database is empty or not
    if not database_array:
        return

    # initialize the variables that will store the final results
    num_students = (len(database_array) // 4)
    highest_mark = 0
    lowest_mark = 100

    # a simple MAX function
    for x in range(3, len(database_array), 4):
        if database_array[x] > highest_mark:
            highest_mark = database_array[x]

    # a simple MIN function
    for x in range(3, len(database_array), 4):
        if database_array[x] < lowest_mark:
            lowest_mark = database_array[x]

    # Print all the statistics using a clean format
    print("--- STATISTICS ---\n\n")
    print(f"Number of students: {num_students}\n"
          f"Highest Mark:       {highest_mark}\n"
          f"Lowest Mark:        {lowest_mark}\n\n")
 


def main():

    # Initialize the student record that will store all the data in a list as instructed in the assignment
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
                if choice > 8 or choice < 1:
                    raise ValueError
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
                sort_students(student_record)
            case 7:
                display_statistics(student_record)
            case 8:
                print("--- Exiting System ---")
                break


            # For testing and my convenience go back and delete line 330 and 331 to access options 9 and 10
            #case 9: # for debug purposes only
            #    student_record = [20, "Zane Lungu", "IT", 76, 21, "Bob Zulu", "Business", 89, 22, "Daniel Mumba", "Forensics", 34, 19, "Ted Musonda", "HR", 58,]
            #case 10: # for debug purposes only
            #    print(student_record)


# Initiates the main function
if __name__ == "__main__":
    main()