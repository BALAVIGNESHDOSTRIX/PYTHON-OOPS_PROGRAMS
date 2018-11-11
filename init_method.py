'''
        In python __init__ method is like a constructor of a class for to initialize the class attribute value
        when object is created.

Programmer_name : BALAVIGNESH.M
Implemented_Date : 11-11-2018
'''

class Employee:

    def __init__(self,name,age,company,designation):
        self.name = name
        self.age = str(age)
        self.company = company
        self.designation = designation

    def Print_all_about_person(self):
        print("Name is:" + self.name)
        print("Age:" + self.age)
        print("Company:" + self.company)
        print("Designation:" + self.designation)

employee = Employee("Balavignesh",22,"MNW","Software engineer")
employee.Print_all_about_person()
