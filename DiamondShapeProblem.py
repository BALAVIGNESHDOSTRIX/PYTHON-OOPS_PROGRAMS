'''
DEVELOPER : BALAVIGNESH.M
IMPLEMENTED DATE: 16-11-2018

        Concept Explanation:
                In python programming Diamond shape problem accours when we using the multiple inheritence
                so we can avoid that problem by choose the order resolution when declaring the base class order in
                dervied class

        Program Explanation:
                I created the 4 classes class A , class B ,class C,class D

                class-B and class-C using the single inheritence form derived from base class-A

                class-D uses multiple inheritence so class-D derived from 2 base classes class-B and class-C

                so here all the class are have to form the Diamond shape inheritence model. so class-D affecting
                this problem because it uses a 2 base classes class-B,C but class-B,C also derived seprately from the
                base class-A. so when you calling the class-D of Numberofwheels() method that executes base class method
                here we should focus the base class order what should go to execute first that is a matter.

                        I have declared the class-B as a first base class for class-D so class-B Numberofwheels() function
                        will executes first.


'''

class A:

    def __init__(self):
        self.numberofwheels = 10

    def Numberofwheels(self):
        print("Number of wheels",self.numberofwheels)

class B(A):

    def Numberofwheels(self):
        print("Got from class B:",self.numberofwheels)

class C(A):

    def Numberofwheels(self):
        print("Got from class C:",self.numberofwheels)

class D(B,C):

    def getDetails(self):
        super().Numberofwheels()

bos = B()
cos = C()
dos = D()

bos.Numberofwheels()
cos.Numberofwheels()
dos.Numberofwheels()
