class Employee:

    def __init__(self, emp_id, name, department, designation):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "department": self.department,
            "designation": self.designation
        }


class Project:

    def __init__(self, project_id, project_name, start_date, deadline, status):
        self.project_id = project_id
        self.project_name = project_name
        self.start_date = start_date
        self.deadline = deadline
        self.status = status

    def to_dict(self):
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "start_date": self.start_date,
            "deadline": self.deadline,
            "status": self.status
        }


class Task:

    def __init__(self, task_id, project_id, task_name,
                 task_description, assigned_to,
                 priority, deadline, status):

        self.task_id = task_id
        self.project_id = project_id
        self.task_name = task_name
        self.task_description = task_description
        self.assigned_to = assigned_to
        self.priority = priority
        self.deadline = deadline
        self.status = status

    def to_dict(self):

        return {
            "task_id": self.task_id,
            "project_id": self.project_id,
            "task_name": self.task_name,
            "task_description": self.task_description,
            "assigned_to": self.assigned_to,
            "priority": self.priority,
            "deadline": self.deadline,
            "status": self.status
        }