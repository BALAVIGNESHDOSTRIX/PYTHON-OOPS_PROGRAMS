'''
        Access Specifier is used to define the class attribute accessing scope at outside of the class

        Access Specifiers:
            public => declare noraml way Ex:=> Myname = "Balavignesh"
            protected => Ex:=> _Myname = "Balavignesh"
            private => Ex:=> __Myname = "Balavignesh"

            Here the variable is 'public' means we can access anywhere in the program . if the varibale declared
            as a 'protected' means we can access within the class and derived class . if the varibale declared as
            a 'private' means we can access only within the class.

            The developer should follow these rules but the python language developer decided the syntax will never
            stop the developers so we can access the private varibale in outside of the class that is called as
            'name mangling' syntax like:=> _classname__(private varibale name) Ex:=> _Car__developedcountry like that

Programmer_name : BALAVIGNESH.M
Implemented_Date : 12-11-2018

'''

class Car:

    carname = "Buggati" #public varibale
    _wheelsc = 4        #protected varibale
    __developedcountry = "Germen" #private varibale

class CarInfo(Car):

    def __init__(self):
        self.funcname = "CarInfoViwer"

    def GetCarInfo(self):
        print("Public varibale access Ex:=> Carname: ",self.carname)
        print("Protected varibale access Ex:=> Number of wheels: ",self._wheelsc)
        print("Private varibale access Ex:=> Made in :",self._Car__developedcountry)

car = CarInfo()
car.GetCarInfo()
