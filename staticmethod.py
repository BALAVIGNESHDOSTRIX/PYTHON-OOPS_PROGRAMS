class Employee:

    def Print_name(self):
        self.name = "mark"
        print(self.name)

    @staticmethod
    def Print_names():
        print("He is the clone of julius ceaser")

employee = Employee()
employee.Print_name()
employee.Print_names()


#In Sttaic method we dont have to use self parameter because the python know by using @staticmethod(decorator) so
#it has ignore the method binding with object
