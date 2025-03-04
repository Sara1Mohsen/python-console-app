import re

class User:
    def __init__(self, name, password, email, phone):
        self.name = name
        self.password = password
        self.email = email
        self.phone = phone

def is_valid_phone(phone):
    pattern = r"^(\+201|01|00201)[0-2,5]{1}[0-9]{8}$"
    return re.fullmatch(pattern, phone) is not None

users = {}

def main():
    print('Select an option: (l)ogin | (s)ignup')
    answer = input().lower()

    user = None  

    while answer not in ['l', 's']:
        print('Invalid option. Please choose (l)ogin or (s)ignup.')
        answer = input().lower()

    if answer == 's':
        userName = input('Create a username: ')
        
        while True:
            passwd = input('Enter a password: ')
            confirmPasswd = input('Confirm password: ')
            if passwd == confirmPasswd:
                break
            print("Passwords do not match. Please re-enter.")

        Email = input('Enter your email: ')

        while True:
            phone = input('Enter your phone number: ')
            if is_valid_phone(phone):
                print('Valid phone number :)')
                break
            print('Invalid phone number. Please enter a valid Egyptian phone number.')

        user = User(userName, passwd, Email, phone)
        users[userName] = {"user_info": user, "projects": []}  
        print('Account Created Successfully! :)\n')
    
    while True:
        print('Select an option: (l)ogin | (s)ignup')
        answer = input().lower()

        if answer == 'l':
            userlogin = input('Enter username: ')
            userpasswd = input('Enter password: ')

            if userlogin not in users:
                print('No account found. Please sign up first.')
                continue

            user = users[userlogin]["user_info"]

            while userpasswd != user.password:
                print('Invalid password')
                userpasswd = input('Enter password: ')

            print('Login Successful! :)')
            logged_in_user = user
            break  

        elif answer == 's':  
            print("You already have an account. Please log in.")
        else:
            print('Invalid option. Please enter (l)ogin or (s)ignup.')

    print(f'Welcome {logged_in_user.name} to the Crowd Funding App! :)')

    while True:
        print("\nChoose an option:")
        print("(1) Create a new project")
        print("(2) View my projects")
        print("(3) Edit a project")
        print("(4) Delete a project")
        print("(5) Logout")

        option = input("Enter your choice: ")

        if option == "1":
            project = CreateProject(logged_in_user)
            project.create_project()
            users[logged_in_user.name]["projects"].append(project)  # Store the project in the user's list

        elif option == "2":
            view_projects(logged_in_user.name)

        elif option == "3":
            edit_project(logged_in_user.name)

        elif option == "4":
            delete_project(logged_in_user.name)

        elif option == "5":
            print("Logging out... Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid choice.")


class CreateProject:
    def __init__(self, user):
        if not user:
            raise ValueError("You must be logged in to create a project.")
        
        self.user = user  
        self.title = ""
        self.description = ""
        self.totalTarget = 0
        self.startDate = ""
        self.endDate = ""

    def is_valid_date(self, date):
        pattern_date = r"^\d{4}-\d{2}-\d{2}$"
        return re.fullmatch(pattern_date, date) is not None

    def create_project(self):
        print(f"\nHello {self.user.name}, let's create your project! :)")

        self.title = input('Enter project title: ')
        self.description = input('Enter project description: ')
        self.totalTarget = input('Enter total target amount: ')

        while True:
            self.startDate = input('Enter start date (YYYY-MM-DD): ')
            self.endDate = input('Enter end date (YYYY-MM-DD): ')

            if self.is_valid_date(self.startDate) and self.is_valid_date(self.endDate):
                print('Valid dates :)')
                break
            print('Invalid date format. Please enter dates in YYYY-MM-DD format.')

        print(f'\nProject "{self.title}" Created Successfully! :)')

def view_projects(username):
    if not users[username]["projects"]:
        print("\nYou have no projects yet.")
    else:
        print("\nYour Projects:")
        for idx, project in enumerate(users[username]["projects"], start=1):
            print(f"\nProject {idx}:")
            print(f"Title: {project.title}")
            print(f"Description: {project.description}")
            print(f"Total Target: {project.totalTarget}")
            print(f"Start Date: {project.startDate}")
            print(f"End Date: {project.endDate}")


def edit_project(username):
    if not users[username]["projects"]:
        print("\nYou have no projects to edit.")
        return
    
    view_projects(username)

    try:
        choice = int(input("\nEnter the project number to edit: ")) - 1
        if choice < 0 or choice >= len(users[username]["projects"]):
            print("Invalid project number.")
            return

        project = users[username]["projects"][choice]

        print("\nEnter new details (leave blank to keep current value):")
        new_title = input(f"New title ({project.title}): ") or project.title
        new_description = input(f"New description ({project.description}): ") or project.description
        new_total_target = input(f"New total target ({project.totalTarget}): ") or project.totalTarget
        
        while True:
            new_start_date = input(f"New start date ({project.startDate}): ") or project.startDate
            new_end_date = input(f"New end date ({project.endDate}): ") or project.endDate

            if CreateProject.is_valid_date(self=None, date=new_start_date) and CreateProject.is_valid_date(self=None, date=new_end_date):
                break
            print("Invalid date format. Please enter dates in YYYY-MM-DD format.")

        project.title = new_title
        project.description = new_description
        project.totalTarget = new_total_target
        project.startDate = new_start_date
        project.endDate = new_end_date

        print("Project updated successfully!")

    except ValueError:
        print("Invalid input. Please enter a valid project number.")



def delete_project(username):
    if not users[username]["projects"]:
        print("\nYou have no projects to delete.")
        return
    
    view_projects(username)

    try:
        choice = int(input("\nEnter the project number to delete: ")) - 1
        if choice < 0 or choice >= len(users[username]["projects"]):
            print("Invalid project number.")
            return
        
        confirmation = input("Are you sure you want to delete this project? (y/n): ").lower()
        if confirmation == "y":
            del users[username]["projects"][choice]
            print("Project deleted successfully!")
        else:
            print("Deletion canceled.")

    except ValueError:
        print("Invalid input. Please enter a valid project number.")

if __name__ == "__main__":
    main()
