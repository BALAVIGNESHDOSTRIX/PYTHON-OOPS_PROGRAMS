'''
            Inheritence is reflecting the base class functionalities to derived or child class

            Real world Explanation:
                A mother have blue eyes her child also have blue eyes because here mother blue eyes are
                inherited to child so child having the same

            Program explanation:
                I have implemented following program it has 2 classes (Infidos , Company) the class
                Infidos have 3 attributes (Product,website,since) these are Infidos company details and
                class Company have 2 method (__init__ => 'like a constructor for initialize the
                class attributes' , GetCompanyDetails => 'get all the company details from super class(Infidos)')

Programmer_name : BALAVIGNESH.M
Implemented_Date : 11-11-2018                
'''

class Infidos:

    Product = "Developing a Computer Software Appplications"
    website = "https://www.infidos.com"
    since = 2020



class Company(Infidos):

    def __init__(self):
        self.companyname = "INFIDOS"

    def GetCompanyDetails(self):
        print("Company Name is : {x}".format(x=self.companyname))
        print("Developing Products :{y}".format(y=self.Product))
        print("Official Website : {f}".format(f=self.website))
        print("Company started Year:{v}".format(v=self.since))


company = Company()
company.GetCompanyDetails()
