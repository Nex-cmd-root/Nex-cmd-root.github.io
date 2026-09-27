def update(course):
    new = input("Enter the new course: ")

    course.append(new)
    print(f"successfully added {new} to the course list.")
    return

def get(course):
    for i in course:
        print(i)
    return

def select(course):
    pull = input("What course would you like to select: ")
    if pull not in course:
        print("course not found")
        return
    i = course.index(pull)
    print(course[i])
    return

def delete(course):
    erase = input("What course do you want to remove: ")
    if erase not in course:
        print("course not found")
        return
    course.remove(erase)
    return

def main():
    course_list = []
    password = "Frost the goat"

    while True:
        try:
            user_input = input("Enter your login credentials")
            if user_input != password:
                raise ValueError
            print("Welcome\n")
            break
        except ValueError:
            print("Invalid login credentials")

    if user_input == password:
        while True:
            print("1. Update Course List")
            print("2. Get Course List")
            print("3. Select a Course")
            print("4. Delete a Course")
            print("5. Exit")

            while True:
                try:
                    choice = int(input("Enter your choice: "))
                    if choice < 1 or choice > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid choice, try 1-5")

            match choice:
                case 1:
                    update(course_list)
                case 2:
                    get(course_list)
                case 3:
                    select(course_list)
                case 4:
                    delete(course_list)
                case 5:
                    print("thank you for using the system")
                    break


if __name__ == "__main__":
    main()