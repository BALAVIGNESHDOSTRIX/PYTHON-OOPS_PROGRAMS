class Employee:
    working_hours_of_person = 6


employee = Employee()
employeeTwo = Employee()

#Class Attribute Example
print(employee.working_hours_of_person)

#Instance Attribute Access Example
employeeTwo.working_hours_of_person = 77
print(employeeTwo.working_hours_of_person)
print(employee.working_hours_of_person)


















#Every time The program should check if any given attribute name is declared as a Instance attribute if yes means
#that will taken first if not means the program should check the class attribute is present then it will print
