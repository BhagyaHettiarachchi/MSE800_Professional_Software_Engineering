from database import create_table
from user_manager import add_user, view_users, search_user, delete_user,advanced_search_user
from course_manager import add_course, search_course, assign_user_to_course, get_courses_by_user

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Advanced Search (by ID and Name)")
    print("7. Add Course)")
    print("8. Search Course (by Course ID and User Name)")
    print("9. Assign User to Course")
    print("10. View User's Courses")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-10): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            users = search_user(user_id if user_id else None, name if name else None)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
        elif choice == '6':
             user_id = input("Enter ID: ").strip()
             name = input("Enter name: ").strip()
             user_id = int(user_id) if user_id else None
             results = advanced_search_user(user_id, name)
             for user in results:
              print(user)
        elif choice == '7':
            course_name = input("Enter course name: ")
            unit = int(input("Enter number of units: "))
            add_course(course_name, unit)
        elif choice == '8':
            course_id_input = input("Enter course ID: ").strip()
            user_name = input("Enter user name to associate: ").strip()
            course_id = int(course_id_input) if course_id_input else None
            results = search_course(course_id, user_name)
            for course in results:
             print(course)
        elif choice == '9':
           user_id = int(input("Enter User ID: "))
           course_id = int(input("Enter Course ID: "))
           assign_user_to_course(user_id, course_id)
        elif choice == '10':
           user_id = int(input("Enter User ID to view courses: "))
           courses = get_courses_by_user(user_id)
        if courses:
           for c in courses:
            print(f"Course ID: {c[0]}, Name: {c[1]}, Unit: {c[2]}")
           else:
            print("No courses found for this user.")
            break
        else:
             print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
