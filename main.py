from employee_manager import *
from project_manager import *
from task_manager import *
from report_manager import *


# -------------------------
# Employee Menu
# -------------------------

def employee_menu():

    while True:

        print("\n========== EMPLOYEE MANAGEMENT ==========")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            break

        else:
            print("Invalid Choice!")


# -------------------------
# Project Menu
# -------------------------

def project_menu():

    while True:

        print("\n========== PROJECT MANAGEMENT ==========")
        print("1. Add Project")
        print("2. View Projects")
        print("3. Search Project")
        print("4. Update Project")
        print("5. Delete Project")
        print("6. Change Project Status")
        print("7. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_project()

        elif choice == "2":
            view_projects()

        elif choice == "3":
            search_project()

        elif choice == "4":
            update_project()

        elif choice == "5":
            delete_project()

        elif choice == "6":
            change_project_status()

        elif choice == "7":
            break

        else:
            print("Invalid Choice!")


# -------------------------
# Task Menu
# -------------------------

def task_menu():

    while True:

        print("\n========== TASK MANAGEMENT ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Task")
        print("4. Update Task")
        print("5. Delete Task")
        print("6. Update Task Status")
        print("7. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            search_task()

        elif choice == "4":
            update_task()

        elif choice == "5":
            delete_task()

        elif choice == "6":
            update_task_status()

        elif choice == "7":
            break

        else:
            print("Invalid Choice!")


# -------------------------
# Reports Menu
# -------------------------

def report_menu():

    while True:

        print("\n========== REPORTS ==========")
        print("1. Dashboard")
        print("2. Employee Report")
        print("3. Project Report")
        print("4. Task Report")
        print("5. Tasks By Employee")
        print("6. Tasks By Project")
        print("7. Pending Tasks")
        print("8. Completed Tasks")
        print("9. Overdue Tasks")
        print("10. Project Progress")
        print("11. Back")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            dashboard()

        elif choice == "2":
            employee_report()

        elif choice == "3":
            project_report()

        elif choice == "4":
            task_report()

        elif choice == "5":
            tasks_by_employee()

        elif choice == "6":
            tasks_by_project()

        elif choice == "7":
            pending_tasks()

        elif choice == "8":
            completed_tasks()

        elif choice == "9":
            overdue_tasks()

        elif choice == "10":
            project_progress()

        elif choice == "11":
            break

        else:
            print("Invalid Choice!")


# -------------------------
# Main Menu
# -------------------------

def main():

    while True:

        print("\n")
        print("=" * 55)
        print("         PROJECT MANAGEMENT SYSTEM")
        print("=" * 55)

        dashboard()

        print("\n1. Employee Management")
        print("2. Project Management")
        print("3. Task Management")
        print("4. Reports")
        print("5. Exit")

        choice = input("\nEnter Choice : ")

        if choice == "1":
            employee_menu()

        elif choice == "2":
            project_menu()

        elif choice == "3":
            task_menu()

        elif choice == "4":
            report_menu()

        elif choice == "5":
            print("\nThank You! Visit Again.")
            break

        else:
            print("Invalid Choice! Please Try Again.")


if __name__ == "__main__":
    main()