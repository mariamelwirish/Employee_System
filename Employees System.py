# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 20:19:50 2023

@author: Mariam Elweresh
"""

"""This project is done by a group of 2 members:
1. Mariam Mohamed Elwirish - 320220076
2. Yousef Mohamed Mohamed Hamed - 320220064"""

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __str__(self):
        return f"{self.name}, {self.age}, {self.salary}"
class EmployeesManager:
    def __init__ (self):
        self.employees = []
    def add_new_employee(self, name, age, salary):
        emp = Employee(name, age, salary)
        self.employees.append(emp)
        print("\n" , "************************")
        print("A new employee has been added.")
        print("\n" , "************************")
    def list_all_employees(self):
        for emp in self.employees:
            print(emp , "\n")
        if self.employees.__len__() == 0:
            print("There are no employees to display. ")
    def delete_employee_by_age_range(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age
        for emp in range (len(self.employees)):
            x = self.employees[emp]
            if x.age in range(min_age, max_age):
                del self.employees[emp]
                print("\n", "Employee has been deleted." , "\n")
            else:
                print("There are no employees with this age range.")
    def update_salary_given_a_name(self, name, newsalary):
        for emp in self.employees:
            if emp.name == name:
               emp.salary = newsalary
            else:
                break
    def make_choice(self, choice):
        if choice == 1:
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            salary = int(input("Enter employee salary: "))
            self.add_new_employee(name, age, salary)
        elif choice == 2:
            self.list_all_employees()
            print("\n")
        elif choice == 3:
            if self.employees.__len__() == 0:
                print("No employees to remove. ")
                print("\n")
            else:
                min_age = int(input("Enter the starting age: "))
                max_age = int(input("Enter the ending age: "))
                self.delete_employee_by_age_range(min_age, max_age)
        elif choice == 4:
            while True:
                if self.employees.__len__() == 0:
                    print("There are no employees to update salary. \n")
                    break
                else:
                    name = input("Enter employee name: ")
                if not any(emp.name == name for emp in self.employees):
                    print("Name doesn't match.")
                else:
                    newsalary = int(input("Enter the new salary: "))
                    self.update_salary_given_a_name(name, newsalary)
                    print("\n","The selected employee's salary has been updated.\n")
                    break
        elif choice == 5:
            print("End of the program.")
            exit()
        else:
            print("Invalid input. Enter a valid input from 1 to 5! ")
class FrontendManager:
    def __init__(self):
        self.emp_manager = EmployeesManager()
    def print_options(self):
        print("Welcome to Employees system. Wish you a nice experience 😁" , "\n")
        print("Program options:")
        print("1) Add new employee")
        print("2) List all employees")
        print("3) Delete by age range")
        print("4) Update salary given a name")
        print("5) End the program")
    def get_option(self):
        while True:
            choice = int(input("Enter your choice (from 1 to 5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid input. Enter a choice from 1 to 5! ")
    def run(self):
        while True:
            self.print_options()
            choice = self.get_option()
            self.emp_manager.make_choice(choice)
if __name__ == "__main__":
    FrontendManager().run()