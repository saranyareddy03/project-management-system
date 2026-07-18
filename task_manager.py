from models import Task
from file_handler import read_csv, write_csv
from utils import (
    generate_task_id,
    employee_exists,
    project_exists,
    validate_name,
    validate_date,
    validate_priority,
    validate_status
)

TASK_FILE = "data/tasks.csv"

FIELDNAMES = [
    "task_id",
    "project_id",
    "task_name",
    "task_description",
    "assigned_to",
    "priority",
    "deadline",
    "status"
]

PRIORITY_OPTIONS = [
    "Low",
    "Medium",
    "High"
]

STATUS_OPTIONS = [
    "Pending",
    "In Progress",
    "Completed"
]


# -------------------------
# Add Task
# -------------------------

def add_task():

    print("\n========== Add Task ==========")

    while True:

        project_id = input("Enter Project ID : ").upper().strip()

        if project_exists(project_id):
            break

        print("Project Not Found!")

    while True:

        assigned_to = input("Assign Employee ID : ").upper().strip()

        if employee_exists(assigned_to):
            break

        print("Employee Not Found!")

    while True:

        task_name = input("Enter Task Name : ").strip()

        if validate_name(task_name):
            break

        print("Task name cannot be empty!")

    task_description = input("Enter Task Description : ").strip()

    while True:

        priority = input("Priority (Low/Medium/High) : ").title().strip()

        if validate_priority(priority):
            break

        print("Invalid Priority!")

    while True:

        deadline = input("Deadline (DD-MM-YYYY) : ").strip()

        if validate_date(deadline):
            break

        print("Invalid Date!")

    status = "Pending"

    task = Task(
        generate_task_id(),
        project_id,
        task_name,
        task_description,
        assigned_to,
        priority,
        deadline,
        status
    )

    tasks = read_csv(TASK_FILE)

    tasks.append(task.to_dict())

    write_csv(
        TASK_FILE,
        tasks,
        FIELDNAMES
    )

    print("\nTask Added Successfully!")
    print("Task ID :", task.task_id)


# -------------------------
# View Tasks
# -------------------------

def view_tasks():

    tasks = read_csv(TASK_FILE)

    if not tasks:
        print("\nNo Tasks Found!")
        return

    print("\n================ TASK LIST ================\n")

    for task in tasks:

        print(f"Task ID       : {task['task_id']}")
        print(f"Project ID    : {task['project_id']}")
        print(f"Task Name     : {task['task_name']}")
        print(f"Description   : {task['task_description']}")
        print(f"Assigned To   : {task['assigned_to']}")
        print(f"Priority      : {task['priority']}")
        print(f"Deadline      : {task['deadline']}")
        print(f"Status        : {task['status']}")
        print("-" * 45)
# -------------------------
# Search Task
# -------------------------

def search_task():

    tasks = read_csv(TASK_FILE)

    if not tasks:
        print("\nNo Tasks Found!")
        return

    task_id = input("Enter Task ID : ").upper().strip()

    for task in tasks:

        if task["task_id"] == task_id:

            print("\n========== TASK FOUND ==========\n")
            print(f"Task ID       : {task['task_id']}")
            print(f"Project ID    : {task['project_id']}")
            print(f"Task Name     : {task['task_name']}")
            print(f"Description   : {task['task_description']}")
            print(f"Assigned To   : {task['assigned_to']}")
            print(f"Priority      : {task['priority']}")
            print(f"Deadline      : {task['deadline']}")
            print(f"Status        : {task['status']}")
            print("-" * 45)
            return

    print("\nTask Not Found!")


# -------------------------
# Update Task
# -------------------------

def update_task():

    tasks = read_csv(TASK_FILE)

    if not tasks:
        print("\nNo Tasks Found!")
        return

    task_id = input("Enter Task ID to Update : ").upper().strip()

    for task in tasks:

        if task["task_id"] == task_id:

            print("\nLeave blank to keep old value.\n")

            task_name = input(
                f"Task Name ({task['task_name']}) : "
            ).strip()

            task_description = input(
                f"Description ({task['task_description']}) : "
            ).strip()

            assigned_to = input(
                f"Assigned Employee ({task['assigned_to']}) : "
            ).upper().strip()

            priority = input(
                f"Priority ({task['priority']}) : "
            ).title().strip()

            deadline = input(
                f"Deadline ({task['deadline']}) : "
            ).strip()

            status = input(
                f"Status ({task['status']}) : "
            ).title().strip()

            if task_name:

                if validate_name(task_name):
                    task["task_name"] = task_name
                else:
                    print("Invalid Task Name!")

            if task_description:
                task["task_description"] = task_description

            if assigned_to:

                if employee_exists(assigned_to):
                    task["assigned_to"] = assigned_to
                else:
                    print("Employee Not Found! Old Employee Retained.")

            if priority:

                if validate_priority(priority):
                    task["priority"] = priority
                else:
                    print("Invalid Priority! Old Priority Retained.")

            if deadline:

                if validate_date(deadline):
                    task["deadline"] = deadline
                else:
                    print("Invalid Date! Old Deadline Retained.")

            if status:

                if validate_status(status, STATUS_OPTIONS):
                    task["status"] = status
                else:
                    print("Invalid Status! Old Status Retained.")

            write_csv(
                TASK_FILE,
                tasks,
                FIELDNAMES
            )

            print("\nTask Updated Successfully!")
            return

    print("\nTask Not Found!")
# -------------------------
# Delete Task
# -------------------------

def delete_task():

    tasks = read_csv(TASK_FILE)

    if not tasks:
        print("\nNo Tasks Found!")
        return

    task_id = input("Enter Task ID to Delete : ").upper().strip()

    for task in tasks:

        if task["task_id"] == task_id:

            confirm = input("Are you sure you want to delete this task? (Y/N): ").upper()

            if confirm == "Y":

                tasks.remove(task)

                write_csv(
                    TASK_FILE,
                    tasks,
                    FIELDNAMES
                )

                print("\nTask Deleted Successfully!")

            else:
                print("\nDeletion Cancelled!")

            return

    print("\nTask Not Found!")


# -------------------------
# Update Task Status
# -------------------------

def update_task_status():

    tasks = read_csv(TASK_FILE)

    if not tasks:
        print("\nNo Tasks Found!")
        return

    task_id = input("Enter Task ID : ").upper().strip()

    for task in tasks:

        if task["task_id"] == task_id:

            print("\nChoose Status")
            print("1. Pending")
            print("2. In Progress")
            print("3. Completed")

            choice = input("Enter Choice : ").strip()

            if choice == "1":
                task["status"] = "Pending"

            elif choice == "2":
                task["status"] = "In Progress"

            elif choice == "3":
                task["status"] = "Completed"

            else:
                print("Invalid Choice!")
                return

            write_csv(
                TASK_FILE,
                tasks,
                FIELDNAMES
            )

            print("\nTask Status Updated Successfully!")
            return

    print("\nTask Not Found!")