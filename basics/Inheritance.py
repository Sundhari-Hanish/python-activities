#Program with a base class Employee and a derived class Manager to demonstrate inheritance
# Base Class
class Employee:
    # Constructor of Employee class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    # Method to calculate bonus (10%)
    def calculate_bonus(self):
        return self.salary * 0.10
# Derived Class (Inheritance)
class Manager(Employee):
    # Manager inherits from Employee
    def __init__(self, name, salary, team_size):
        # Calling parent class constructor directly
        Employee.__init__(self, name, salary)
        self.team_size = team_size

    # Method Overriding
    # Manager gets 20% bonus instead of 10%
    def calculate_bonus(self):
        return self.salary * 0.20
# Main Program
emp = Employee("Arjun", 50000)
mgr = Manager("Priya", 80000, 5)
# Displaying results
print("Employee Name:", emp.name)
print("Employee Bonus:", emp.calculate_bonus())
print("\nManager Name:", mgr.name)
print("Manager Bonus:", mgr.calculate_bonus())
#Manager(Employee) shows inheritance.


