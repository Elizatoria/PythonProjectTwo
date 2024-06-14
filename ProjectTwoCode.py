from datetime import datetime
import datetime

'''
You are tasked to build an employee management system for a small business.
The system allows the business to store and manage employee data and perform tasks related to employee management, 
such as adding and removing employees, updating employee information, 
searching for employees by name or department, and calculating total salary expenses. 
You will need to create one class for this project: Employee, which represents a single employee.

Attributes:
● name: string
● job_title: string
● department: string
● salary: float
● hire_year: int

Methods:
● __str__():  return a string representation.
● years_worked():  return the total years this employee has 
worked here, based on the hire year.
● total_expense():  calculate the total salary expense for this 
employee, which is the salary multiplied by the years worked.
● write_employees():  Write your employee information to a text 
file.
● Add accessor and mutator methods for each attribute so a user 
doesn't need to access them directly. 
● Be sure to use type hinting and a docstring in your class
'''
class Employee:
    # Initializer with Attributes
    def __init__(self, name: str, job_title: str, department: str, salary: float, hire_year: int):
        self.name = name
        self.job_title = job_title
        self.department = department
        self.salary = salary
        self.hire_year = hire_year

    # __str__():  return a string representation
    def __str__(self):
        return f'Employee Name: {self.name}\nJob Title: {self.job_title}\nDepartment: {self.department}\nSalary: ${self.salary:.02f}\nHire Year: {self.hire_year}'
    
    # years_worked():  return the total years this employee has worked here, based on the hire year.
    def years_worked(self):
        today = datetime.datetime.now()
        year = today.year
        return year - self.hire_year
    
    # total_expense():  calculate the total salary expense for this employee, which is the salary multiplied by the years worked.
    def total_expense(self):
        total_expense = self.salary * self.years_worked()
        return f'Total Expense for {self.name} is ${total_expense:.02f}.'
    
    # write_employees():  Write your employee information to a text file.
    def write_employees(self):
        f = open('employee_details.txt', 'w')
        f.write(f'Employee Name: {self.name}\nJob Title: {self.job_title}\nDepartment: {self.department}\nSalary: ${self.salary:.02f}\nHire Year: {self.hire_year}\nYears Worked: {self.years_worked()}\nTotal Expense: {self.total_expense()}')
        f.close()

    # Accessor Method
    def get_name(self):
        print(self.name)
    
    def get_job_title(self):
        print(self.job_title)
    
    def get_department(self):
        print(self.department)
    
    def get_salary(self):
        print(self.salary)
    
    def get_hire_year(self):
        print(self.hire_year)
    
    # Mutator Method - Setter
    def set_name(self, new_name: str):
        self.name = new_name

    def set_job_title(self, new_job_title: str):
        self.job_title = new_job_title

    def set_department(self, new_department: str):
        self.department = new_department

    def set_salary(self, new_salary: float):
        self.salary = new_salary
    
    def set_hire_year(self, new_hire_year: int):
        self.hire_year = new_hire_year

# Creates our first Object of the Employee Class
employee1 = Employee('Xylia Pietas', 'Data Scientist', 'Data Analysis', 124360, 2011)

# # String Representation
# print(employee1)

# # How many years worked at the Company
# print(f'Years Worked: {employee1.years_worked()}')

# # Total Expense of the Employee
# print(employee1.total_expense())

# # Write Employees
# employee1.write_employees()

# # Getting with Accessor Method
# employee1.get_name()
# employee1.get_job_title()
# employee1.get_department()
# employee1.get_salary()
# employee1.get_hire_year()

# # Setting with Mutator Method
# employee1.set_name('Xylia Esquivel')
# employee1.set_job_title('Database Engineer')
# employee1.set_department('Computer Information Systems')
# employee1.set_salary(130306)
# employee1.set_hire_year(2013)
# print(employee1)