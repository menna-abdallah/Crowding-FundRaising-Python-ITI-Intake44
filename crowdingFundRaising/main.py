import json
from functions.users import Auth
from functions.projects import create_project,show_all, update_project, delete_project,search_projects_by_date

def main():
    auth = Auth()
    current_user = None
    flag = True
    while flag:
        print("\nMain Menu:")
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            auth.signup()
        elif choice == '2':
            current_user = auth.login()
            if current_user:
                project_functions_menu(current_user)
        elif choice == '3':
            auth.logout()
            flag = False
        else:
            print("Invalid choice. Please try again.")

def project_functions_menu(current_user):
    flag = True
    while flag:
        print("\nProject Functions Menu:")
        print("1. Create Project")
        print("2. View All Projects")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. search")
        print("6. logOut")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_project(current_user)
        elif choice == '2':
            show_all(current_user)
        elif choice == '3':
            update_project(current_user)
        elif choice == '4':
            delete_project(current_user)
        elif choice == '5':
            search_projects_by_date(current_user)
        elif choice == '6':
            print("Logged out successfully.")
            flag = False
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

