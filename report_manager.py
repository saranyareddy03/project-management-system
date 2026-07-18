from file_handler import read_csv
from datetime import datetime

EMPLOYEE_FILE = "data/employees.csv"
PROJECT_FILE = "data/projects.csv"
TASK_FILE = "data/tasks.csv"


# -------------------------
# Dashboard
# -------------------------

def dashboard():

    employees = read_csv(EMPLOYEE_FILE)
    projects = read_csv(PROJECT_FILE)
    tasks = read_csv(TASK_FILE)

    pending = 0
    completed = 0
    in_progress = 0

    project_completed = 0
    project_progress = 0
    project_not_started = 0

    for task in tasks:

        if task["status"] == "Pending":
            pending += 1

        elif task["status"] == "Completed":
            completed += 1

        elif task["status"] == "In Progress":
            in_progress += 1

    for project in projects:

        if project["status"] == "Completed":
            project_completed += 1

        elif project["status"] == "In Progress":
            project_progress += 1

        elif project["status"] == "Not Started":
            project_not_started += 1

    print("\n" + "=" * 50)
    print("               DASHBOARD")
    print("=" * 50)

    print(f"Total Employees        : {len(employees)}")
    print(f"Total Projects         : {len(projects)}")
    print(f"Total Tasks            : {len(tasks)}")

    print("-" * 50)

    print(f"Pending Tasks          : {pending}")
    print(f"In Progress Tasks      : {in_progress}")
    print(f"Completed Tasks        : {completed}")

    print("-" * 50)

    print(f"Projects Not Started   : {project_not_started}")
    print(f"Projects In Progress   : {project_progress}")
    print(f"Completed Projects     : {project_completed}")

    print("=" * 50)


# -------------------------
# Employee Report
# -------------------------

def employee_report():

    employees = read_csv(EMPLOYEE_FILE)

    if not employees:
        print("\nNo Employees Found!")
        return

    print("\n========== EMPLOYEE REPORT ==========\n")

    for employee in employees:

        print(f"{employee['emp_id']} | {employee['name']} | {employee['department']} | {employee['designation']}")


# -------------------------
# Project Report
# -------------------------

def project_report():

    projects = read_csv(PROJECT_FILE)

    if not projects:
        print("\nNo Projects Found!")
        return

    print("\n========== PROJECT REPORT ==========\n")

    for project in projects:

        print(f"{project['project_id']} | {project['project_name']} | {project['start_date']} | {project['deadline']} | {project['status']}")


# -------------------------
# Task Report
# -------------------------

def task_report():

    tasks = read_csv(TASK_FILE)

    if not tasks:
        print("\nNo Tasks Found!")
        return

    print("\n========== TASK REPORT ==========\n")

    for task in tasks:

        print(f"{task['task_id']} | {task['task_name']} | {task['assigned_to']} | {task['priority']} | {task['status']}")


# -------------------------
# Tasks By Employee
# -------------------------

def tasks_by_employee():

    emp_id = input("Enter Employee ID : ").upper()

    tasks = read_csv(TASK_FILE)

    found = False

    print("\n========== TASKS ==========\n")

    for task in tasks:

        if task["assigned_to"] == emp_id:

            found = True

            print(f"{task['task_id']} | {task['task_name']} | {task['priority']} | {task['status']}")

    if not found:
        print("No Tasks Assigned.")


# -------------------------
# Tasks By Project
# -------------------------

def tasks_by_project():

    project_id = input("Enter Project ID : ").upper()

    tasks = read_csv(TASK_FILE)

    found = False

    print("\n========== TASKS ==========\n")

    for task in tasks:

        if task["project_id"] == project_id:

            found = True

            print(f"{task['task_id']} | {task['task_name']} | {task['assigned_to']} | {task['status']}")

    if not found:
        print("No Tasks Found.")


# -------------------------
# Pending Tasks
# -------------------------

def pending_tasks():

    tasks = read_csv(TASK_FILE)

    print("\n========== PENDING TASKS ==========\n")

    found = False

    for task in tasks:

        if task["status"] == "Pending":

            found = True

            print(f"{task['task_id']} | {task['task_name']} | {task['assigned_to']}")

    if not found:
        print("No Pending Tasks.")


# -------------------------
# Completed Tasks
# -------------------------

def completed_tasks():

    tasks = read_csv(TASK_FILE)

    print("\n========== COMPLETED TASKS ==========\n")

    found = False

    for task in tasks:

        if task["status"] == "Completed":

            found = True

            print(f"{task['task_id']} | {task['task_name']} | {task['assigned_to']}")

    if not found:
        print("No Completed Tasks.")


# -------------------------
# Overdue Tasks
# -------------------------

def overdue_tasks():

    tasks = read_csv(TASK_FILE)

    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    found = False

    print("\n========== OVERDUE TASKS ==========\n")

    for task in tasks:

        try:

            deadline = datetime.strptime(task["deadline"], "%d-%m-%Y")

            if deadline < today and task["status"] != "Completed":

                found = True

                print(f"{task['task_id']} | {task['task_name']} | {task['deadline']} | {task['status']}")

        except:
            continue

    if not found:
        print("No Overdue Tasks.")


# -------------------------
# Project Progress
# -------------------------

def project_progress():

    projects = read_csv(PROJECT_FILE)
    tasks = read_csv(TASK_FILE)

    print("\n========== PROJECT PROGRESS ==========\n")

    for project in projects:

        total = 0
        completed = 0

        for task in tasks:

            if task["project_id"] == project["project_id"]:

                total += 1

                if task["status"] == "Completed":
                    completed += 1

        if total == 0:
            percent = 0
        else:
            percent = round((completed / total) * 100)

        print(f"{project['project_id']} | {project['project_name']} | {percent}% Completed")