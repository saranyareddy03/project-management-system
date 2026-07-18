from models import Project
from file_handler import read_csv, write_csv
from utils import (
    generate_project_id,
    get_today,
    validate_name,
    validate_date,
    validate_status,
    project_has_tasks
)

PROJECT_FILE = "data/projects.csv"

FIELDNAMES = [
    "project_id",
    "project_name",
    "start_date",
    "deadline",
    "status"
]

STATUS_OPTIONS = [
    "Not Started",
    "In Progress",
    "Completed"
]


# -------------------------
# Add Project
# -------------------------

def add_project():

    print("\n========== Add Project ==========")

    while True:
        project_name = input("Enter Project Name : ").strip()

        if validate_name(project_name):
            break

        print("Project Name cannot be empty!")

    start_date = get_today()

    while True:
        deadline = input("Enter Deadline (DD-MM-YYYY): ").strip()

        if validate_date(deadline):
            break

        print("Invalid Date Format!")

    status = "Not Started"

    project = Project(
        generate_project_id(),
        project_name,
        start_date,
        deadline,
        status
    )

    projects = read_csv(PROJECT_FILE)
    projects.append(project.to_dict())

    write_csv(PROJECT_FILE, projects, FIELDNAMES)

    print("\nProject Added Successfully!")
    print("Project ID :", project.project_id)


# -------------------------
# View Projects
# -------------------------

def view_projects():

    projects = read_csv(PROJECT_FILE)

    if not projects:
        print("\nNo Projects Found!")
        return

    print("\n========== PROJECT LIST ==========\n")

    for project in projects:

        print(f"Project ID   : {project['project_id']}")
        print(f"Project Name : {project['project_name']}")
        print(f"Start Date   : {project['start_date']}")
        print(f"Deadline     : {project['deadline']}")
        print(f"Status       : {project['status']}")
        print("-" * 45)


# -------------------------
# Search Project
# -------------------------

def search_project():

    projects = read_csv(PROJECT_FILE)

    if not projects:
        print("\nNo Projects Found!")
        return

    project_id = input("Enter Project ID : ").upper().strip()

    for project in projects:

        if project["project_id"] == project_id:

            print("\nProject Found")
            print("-" * 45)
            print(f"Project ID   : {project['project_id']}")
            print(f"Project Name : {project['project_name']}")
            print(f"Start Date   : {project['start_date']}")
            print(f"Deadline     : {project['deadline']}")
            print(f"Status       : {project['status']}")
            print("-" * 45)
            return

    print("\nProject Not Found!")


# -------------------------
# Update Project
# -------------------------

def update_project():

    projects = read_csv(PROJECT_FILE)

    if not projects:
        print("\nNo Projects Found!")
        return

    project_id = input("Enter Project ID : ").upper().strip()

    for project in projects:

        if project["project_id"] == project_id:

            print("\nLeave blank to keep old value.\n")

            name = input(f"Project Name ({project['project_name']}): ").strip()

            deadline = input(f"Deadline ({project['deadline']}): ").strip()

            status = input(
                f"Status ({project['status']}) [Not Started/In Progress/Completed]: "
            ).strip()

            if name:
                
                if validate_name(name):
                    project["project_name"] = name
                else:
                    print("Invalid Project Name!")
            if deadline:
                
                if validate_date(deadline):
                    project["deadline"] = deadline
                else:
                    print("Invalid date! Old deadline retained.")

            if status:

                if validate_status(status, STATUS_OPTIONS):
                    project["status"] = status
                else:
                    print("Invalid status! Old status retained.")

            write_csv(PROJECT_FILE, projects, FIELDNAMES)

            print("\nProject Updated Successfully!")
            return

    print("\nProject Not Found!")


# -------------------------
# Delete Project
# -------------------------

def delete_project():

    projects = read_csv(PROJECT_FILE)

    if not projects:
        print("\nNo Projects Found!")
        return

    project_id = input("Enter Project ID : ").upper().strip()

    if project_has_tasks(project_id):
        print("\nCannot delete project.")
        print("Tasks are assigned to this project.")
        return

    for project in projects:

        if project["project_id"] == project_id:

            confirm = input("Are you sure? (Y/N): ").upper()

            if confirm == "Y":

                projects.remove(project)

                write_csv(PROJECT_FILE, projects, FIELDNAMES)

                print("\nProject Deleted Successfully!")

            else:
                print("\nDeletion Cancelled!")

            return

    print("\nProject Not Found!")


# -------------------------
# Change Project Status
# -------------------------

def change_project_status():

    projects = read_csv(PROJECT_FILE)

    if not projects:
        print("\nNo Projects Found!")
        return

    project_id = input("Enter Project ID : ").upper().strip()

    for project in projects:

        if project["project_id"] == project_id:

            print("\n1. Not Started")
            print("2. In Progress")
            print("3. Completed")

            choice = input("Enter Choice : ")

            if choice == "1":
                project["status"] = "Not Started"

            elif choice == "2":
                project["status"] = "In Progress"

            elif choice == "3":
                project["status"] = "Completed"

            else:
                print("Invalid Choice!")
                return

            write_csv(PROJECT_FILE, projects, FIELDNAMES)

            print("\nProject Status Updated Successfully!")
            return

    print("\nProject Not Found!")