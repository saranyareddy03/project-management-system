from datetime import datetime
from file_handler import read_csv

EMPLOYEE_FILE = "data/employees.csv"
PROJECT_FILE = "data/projects.csv"
TASK_FILE = "data/tasks.csv"


# -------------------------------
# Generate Employee ID
# -------------------------------
def generate_employee_id():
    employees = read_csv(EMPLOYEE_FILE)

    if not employees:
        return "E101"

    max_id = 100

    for employee in employees:
        try:
            number = int(employee["emp_id"][1:])
            if number > max_id:
                max_id = number
        except:
            pass

    return f"E{max_id + 1}"


# -------------------------------
# Generate Project ID
# -------------------------------
def generate_project_id():
    projects = read_csv(PROJECT_FILE)

    if not projects:
        return "P101"

    max_id = 100

    for project in projects:
        try:
            number = int(project["project_id"][1:])
            if number > max_id:
                max_id = number
        except:
            pass

    return f"P{max_id + 1}"


# -------------------------------
# Generate Task ID
# -------------------------------
def generate_task_id():
    tasks = read_csv(TASK_FILE)

    if not tasks:
        return "T101"

    max_id = 100

    for task in tasks:
        try:
            number = int(task["task_id"][1:])
            if number > max_id:
                max_id = number
        except:
            pass

    return f"T{max_id + 1}"


# -------------------------------
# Today's Date
# -------------------------------
def get_today():
    return datetime.now().strftime("%d-%m-%Y")


# -------------------------------
# Name Validation
# -------------------------------
def validate_name(name):
    return bool(name.strip())


# -------------------------------
# Date Validation
# -------------------------------
def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


# -------------------------------
# Priority Validation
# -------------------------------
def validate_priority(priority):
    priority = priority.title()
    return priority in ["Low", "Medium", "High"]


# -------------------------------
# Status Validation
# -------------------------------
def validate_status(status, options):
    return status in options


# -------------------------------
# Employee Exists
# -------------------------------
def employee_exists(emp_id):
    employees = read_csv(EMPLOYEE_FILE)

    for employee in employees:
        if employee["emp_id"] == emp_id:
            return True

    return False


# -------------------------------
# Project Exists
# -------------------------------
def project_exists(project_id):
    projects = read_csv(PROJECT_FILE)

    for project in projects:
        if project["project_id"] == project_id:
            return True

    return False


# -------------------------------
# Employee Has Tasks
# -------------------------------
def employee_has_tasks(emp_id):
    tasks = read_csv(TASK_FILE)

    for task in tasks:
        if task["assigned_to"] == emp_id:
            return True

    return False


# -------------------------------
# Project Has Tasks
# -------------------------------
def project_has_tasks(project_id):
    tasks = read_csv(TASK_FILE)

    for task in tasks:
        if task["project_id"] == project_id:
            return True

    return False