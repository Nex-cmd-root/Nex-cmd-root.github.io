def add_student(database_array):
    print("--- Adding new student ---\n")
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
            print("\n")
            break
        except ValueError:
            print("Invalid input entered.\n")

    database_array.extend([student_id, name, program, mark])
    print(f"--- Successfully added {name} to the database ---\n")

    return


def view_students(database_array):

    if not database_array:
        print("The student record is currently empty\n")
        return

    for i in range(0, len(database_array), 4):
        print(f"Student ID: {database_array[i]}\n"
              f"Student Name: {database_array[i+1]}\n"
              f"Student Program: {database_array[i+2]}\n"
              f"Overall Mark: {database_array[i+3]}\n")
    return


def update_student(database_array):

    while True:
        try:
            id = int(input("Enter the student ID for the record you want to update."))
            print("\n")
            break
        except ValueError:
            print("Please enter a valid numerical user ID\n")

    if id in database_array:
        i = database_array.index(id)
        print(f"{id} has been found for student {database_array[(i + 1)]}, what would you like to do:\n")
    else:
        print("Selected id is not in the student record, please try again.\n")
        return

    print("1. Modify Name,\n 2. Change program,\n 3. Edit overall mark\n\n")
    while True:
        try:
            choice = int(input("Your choice: "))
            print("\n")
            break
        except ValueError:
            print("Please Enter a valid choice (1, 2, 3).\n")

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
    while True:
        try:
            id = int(input("Enter the student ID for the record you want to delete."))
            print("\n")
            break
        except ValueError:
            print("Please enter a valid numerical user ID\n")

    if id in database_array:
        i = database_array.index(id)
        print(f"{id} has been found for student {database_array[(i + 1)]}.\n")
    else:
        print(f"{id} is not saved in the student record.")
        return

    while True:
        choice = input(f"Are you sure you want to delete {database_array[(i + 1)]}'s record y/n?")
        if choice == "y":
            del database_array[i:(i + 4)]
            print("\n")
            return
        elif choice == "n":
            print("\n")
            return
        else:
            print("unrecognized input, enter y or n.\n")


def search_student(database_array):
    query = input("Enter student name or ID: ")
    
    target = int(query) if query.isdigit() else query

    if target not in database_array:
        print(f"{query} not found in student record.\n")
        return

    i = database_array.index(target)
    
    if isinstance(target, str):
        i = i - 1

    print(f"Student ID: {database_array[i]}\n"
          f"Student Name: {database_array[i+1]}\n"
          f"Student Program: {database_array[i+2]}\n"
          f"Overall Mark: {database_array[i+3]}\n")
    
    return


def sort_students(database_array):
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

    match choice:
        case 1:
            alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
            alphabet_upper = [letter.upper() for letter in alphabet_lower]

            temp_storage = []
            ordered_pair = []
            result = []

            for i in range(1, len(database_array), 4):
                temp = database_array[i]
                if temp[0] in alphabet_upper:
                    index = alphabet_upper.index(temp[0])
                else:
                    index = alphabet_lower.index(temp[0])
                temp_storage.extend([index])
                linked = list((temp, temp_storage[i // 4]))
                ordered_pair.extend([linked])

            ordered_pair.sort(key=lambda x: x[1])

            temp_storage = []
            for x in range(0, len(ordered_pair)):
                temp = ordered_pair[x][0]
                temp_storage.extend([temp])

            for x in temp_storage:
                index = database_array.index(x)
                result.extend([database_array[index - 1], database_array[index], database_array[index + 1], database_array[index + 2]])

            database_array[:] = result

            print("--- Successfully sorted all students ---")

        case 2:
            storage = []
            temp = []

            for x in range(3, len(database_array), 4):
                temp.extend([database_array[x]])

            temp.sort(reverse = True)
            for x in temp:
                index = database_array.index(x)
                storage.extend([database_array[index - 3], database_array[index - 2], database_array[index - 1], database_array[index],])

            database_array[:] = storage

            print("--- successfully sorted all students ---")

        case 3:
            storage = []
            temp = []

            for x in range(0, len(database_array), 4):
                temp.extend([database_array[x]])

            temp.sort()
            for x in temp:
                index = database_array.index(x)
                storage.extend([database_array[index], database_array[index + 1], database_array[index + 2], database_array[index + 3],])

            database_array[:] = storage

            print("--- successfully sorted all students ---")

    return


def display_statistics(database_array):
    if not database_array:
        return

    num_students = (len(database_array) // 4)
    highest_mark = 0
    lowest_mark = 100

    for x in range(3, len(database_array), 4):
        if database_array[x] > highest_mark:
            highest_mark = database_array[x]

    for x in range(3, len(database_array), 4):
        if database_array[x] < lowest_mark:
            lowest_mark = database_array[x]

    print("--- STATISTICS ---\n\n")
    print(f"Number of students: {num_students}\n"
          f"Highest Mark:       {highest_mark}\n"
          f"Lowest Mark:        {lowest_mark}\n\n")


def main():

    student_record = []

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
        while True:
            try:
                choice = int(input("Enter your choice:"))
                if choice > 8 or choice < 1:
                    raise ValueError
                print("\n")
                break
            except ValueError:
                print("Please enter a valid choice from 1 - 8.\n")

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


if __name__ == "__main__":
    main()