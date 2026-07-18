from models import Employee
from file_handler import read_csv, write_csv
from utils import (
    generate_employee_id,
    validate_name,
    employee_has_tasks
)

EMPLOYEE_FILE = "data/employees.csv"

FIELDNAMES = [
    "emp_id",
    "name",
    "department",
    "designation"
]


# -------------------------
# Add Employee
# -------------------------

def add_employee():

    print("\n========== Add Employee ==========")

    while True:

        name = input("Enter Employee Name : ").strip()

        if validate_name(name):
            break

        print("Employee name cannot be empty!")

    while True:

        department = input("Enter Department : ").strip()

        if department:
            break

        print("Department cannot be empty!")

    while True:

        designation = input("Enter Designation : ").strip()

        if designation:
            break

        print("Designation cannot be empty!")

    employee = Employee(
        generate_employee_id(),
        name,
        department,
        designation
    )

    employees = read_csv(EMPLOYEE_FILE)
    employees.append(employee.to_dict())

    write_csv(
        EMPLOYEE_FILE,
        employees,
        FIELDNAMES
    )

    print("\nEmployee Added Successfully!")
    print("Employee ID :", employee.emp_id)


# -------------------------
# View Employees
# -------------------------

def view_employees():

    employees = read_csv(EMPLOYEE_FILE)

    if not employees:
        print("\nNo Employees Found!")
        return

    print("\n========== EMPLOYEE LIST ==========\n")

    for employee in employees:

        print(f"Employee ID : {employee['emp_id']}")
        print(f"Name        : {employee['name']}")
        print(f"Department  : {employee['department']}")
        print(f"Designation : {employee['designation']}")
        print("-" * 40)


# -------------------------
# Search Employee
# -------------------------

def search_employee():

    employees = read_csv(EMPLOYEE_FILE)

    if not employees:
        print("\nNo Employees Found!")
        return

    emp_id = input("Enter Employee ID : ").upper()

    for employee in employees:

        if employee["emp_id"] == emp_id:

            print("\nEmployee Found")
            print("-" * 40)
            print(f"Employee ID : {employee['emp_id']}")
            print(f"Name        : {employee['name']}")
            print(f"Department  : {employee['department']}")
            print(f"Designation : {employee['designation']}")
            print("-" * 40)
            return

    print("\nEmployee Not Found!")


# -------------------------
# Update Employee
# -------------------------

def update_employee():

    employees = read_csv(EMPLOYEE_FILE)

    if not employees:
        print("\nNo Employees Found!")
        return

    emp_id = input("Enter Employee ID : ").upper()

    for employee in employees:

        if employee["emp_id"] == emp_id:

            print("\nLeave blank to keep old value.\n")

            name = input(f"Name ({employee['name']}): ").strip()
            department = input(f"Department ({employee['department']}): ").strip()
            designation = input(f"Designation ({employee['designation']}): ").strip()

            if name:

                if validate_name(name):
                    employee["name"] = name
                else:
                    print("Invalid Name!")

            if department:
                employee["department"] = department

            if designation:
                employee["designation"] = designation

            write_csv(
                EMPLOYEE_FILE,
                employees,
                FIELDNAMES
            )

            print("\nEmployee Updated Successfully!")
            return

    print("\nEmployee Not Found!")


# -------------------------
# Delete Employee
# -------------------------

def delete_employee():

    employees = read_csv(EMPLOYEE_FILE)

    if not employees:
        print("\nNo Employees Found!")
        return

    emp_id = input("Enter Employee ID : ").upper()

    if employee_has_tasks(emp_id):
        print("\nCannot delete employee.")
        print("Employee has assigned tasks.")
        return

    for employee in employees:

        if employee["emp_id"] == emp_id:

            confirm = input("Are you sure? (Y/N): ").upper()

            if confirm == "Y":

                employees.remove(employee)

                write_csv(
                    EMPLOYEE_FILE,
                    employees,
                    FIELDNAMES
                )

                print("\nEmployee Deleted Successfully!")

            else:
                print("\nDeletion Cancelled!")

            return

    print("\nEmployee Not Found!")