# import sqlite3

# conn = sqlite3.connect('employees.db')
# cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS employees (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         department TEXT,
#         salary REAL
#     )
# ''')

# cursor.executemany('''
#     INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)
# ''', [
#     ('John Doe', 'HR', 50000),
#     ('Jane Smith', 'IT', 60000),
#     ('Emily Davis', 'Finance', 70000),
#     ('Michael Brown', 'IT', 80000),
#     ('Sarah Wilson', 'HR', 45000),
#     ('David Jones', 'Finance', 75000)
# ])

# conn.commit()

# cursor.execute('SELECT AVG(salary) FROM employees')
# avg_salary = cursor.fetchone()[0]
# print(f'Average salary of all employees: {avg_salary:.2f}')

# cursor.execute('SELECT department, COUNT(*) FROM employees GROUP BY department')
# department_counts = cursor.fetchall()
# print('\nCount of employees in each department:')
# for department, count in department_counts:
#     print(f'{department}: {count}')

# cursor.execute('SELECT MAX(salary) FROM employees')
# max_salary = cursor.fetchone()[0]
# print(f'\nMaximum salary of all employees: {max_salary:.2f}')

# cursor.execute('SELECT SUM(salary) FROM employees')
# total_salary = cursor.fetchone()[0]
# print(f'\nSum of salaries of all employees: {total_salary:.2f}')

# conn.close()



class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus

class EmployeeOne:
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age

        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = EmployeeOne('Samuel', 22, 25000, 8500)

print(emp.total_salary())
