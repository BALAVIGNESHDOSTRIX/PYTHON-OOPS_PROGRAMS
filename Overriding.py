'''

DEVELOPER NAME: BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018
'''

class Car:

    def Numberofwheels(self):
        self.numberofcarwheels = 4
        print("Number of wheels:",self.numberofcarwheels)

class company(Car):

    def Numberofwheels(self):
        self.numberofcarwheels = 10
        print("Number of wheels:",self.numberofcarwheels)

    def Ovveridewheels(self):
        super().Numberofwheels()


car = Car()
car.Numberofwheels()

com = company()
com.Ovveridewheels()
