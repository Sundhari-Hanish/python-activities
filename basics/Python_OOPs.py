Python – OOPs (Object-Oriented Programming)

Question 1:
Create a Student class with the following requirements:
- Attributes: name, roll_number, marks
- A method display_info() that prints the student details
- A method is_passed() that returns True if marks are 40 or above,
  otherwise False
Create an object of the class and test both methods.

class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

    def is_passed(self):
        return self.marks >= 40
student1 = Student("Arun", 101, 75)
student1.display_info()
print("Passed:", student1.is_passed())

Output:
Name: Arun
Roll Number: 101
Marks: 75
Passed: True


Question 2:
Create a BankAccount class with:
- Attributes: account_holder, balance
- Method deposit(amount) to add money
- Method withdraw(amount) that subtracts money if sufficient balance exists
- Method display_balance() to show current balance
Create an object and perform deposit and withdrawal operations.


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(f"Current Balance: {self.balance}")
account = BankAccount("John")
account.deposit(500)
account.withdraw(200)
account.display_balance()

Output:
Deposited: 500
Withdrawn: 200
Current Balance: 300
