
# Problem1

class Employee:
    def __init__(self, emp_name, emp_id, emp_salary, emp_department):
        self.name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        old_department = self.emp_department
        self.emp_department = new_department
        print(f"Employee department changed from {old_department} to {new_department} successfully...\n")

    def print_details(self):
        print("Employee ID: ", self.emp_id)
        print("Employee name: ", self.name)
        print("Department: ", self.emp_department)
        print("Salary: ", self.emp_salary)
        print("")
    
    def calculate_salary(self, salary, hours_worked):
        salary = self.emp_salary
        # hours_worked = int("Enter total hours worked by the employee: ")
        overtime = hours_worked - 50
        overtime_amt = overtime*(salary/50)
        print(f"The total hours worked by the employee is {hours_worked}, and overtime worked is {overtime}.\n")
        print(f"Total amount as overtime ${overtime_amt} will be credit with the employee salary. Total payable salary of the employee is ${salary+overtime_amt}.\n")

emp1 = Employee("Samuel", 2345, 80000, 'Fullstack')

emp1.print_details()

emp1.assign_department("Data Science")

emp1.print_details()

emp1.calculate_salary(emp1.emp_salary, 64)