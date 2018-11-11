'''
            Abstraction to achive the Encapsulation (Only provide the application usage to use hiding the implementation details)
            so i created the simple LibraryManagement System for understanding


            Real world example with explanation:
                we all are using the car so if we need to stop the car means simply press the break of the car the car will get
                stopped. here we dont know how the break system is working. how the hydralic breaking system will stop the tire we dont
                know. so here the car company hiding the implementation or working details of breaking system to User these is called as
                Encapsulation and usage of break badale is the abstraction because user only seeing that only inside the car.


            Program Explanation:
                I have implemented the simple LibraryManagement system here i have created the 2 classes (LibraryManagement,Customer) and LibraryManagement
                class have 3 following methods (DisplayAllBooks=> 'Display all availabe books', LendingTheBooks => 'Used to get the book from Library by user',
                AddTheBooks => 'These will helps to add book to Library book list when user book returning time.') and class Customer have 2 methods (TakeBook => '
                Used to requesting the book have to take from Library by the user', ReturnTheBook => 'Used to return the taken book when user have returning time.')

Programmer_name : BALAVIGNESH.M
Implemented_Date : 11-11-2018

'''

class LibraryManagement:

    def __init__(self,booklist):
        self.book_list = booklist

    def DisplayAllBooks(self):
        print()
        print("########  Available Books ##########")

        for book in self.book_list:
            print(book)

    def LendingTheBooks(self,requestedbook):
        if requestedbook in self.book_list:
            self.book_list.remove(requestedbook)
            print("You are successfully got the requested book.")
        else:
            print("Your Requested book is not availabe so please come after or choose another one.")

    def AddTheBooks(self,returnnbook):
        if returnnbook not in self.book_list:
            self.book_list.append(returnnbook)
            print("You are successfully returned the book.")
            print("Thankyou.....!")
        else:
            print("You cant return the book because the book is already available or you are not taken already.")

class Customer:

    def TakeBook(self):
        self.requested_book = str(input("Enter the book name you want to take:"))
        return self.requested_book

    def ReturnTheBook(self):
        self.returnbookname = str(input("Enter the book you have to return:"))
        return self.returnbookname

Library = LibraryManagement(["Men in Black","Harmur of God","The little Child","The 3rd Person"])
Customer = Customer()

while True:
    print("Enter option- 1 for Display all the books")
    print("Enter option- 2 for Taking the book")
    print("Enter option- 3 for Return the book")
    print("Enter the option- 4 for Quit")
    userchoice = int(input("Enter the option to process:"))

    if userchoice is 1:
        Library.DisplayAllBooks()
    elif userchoice is 2:
        bookname = Customer.TakeBook()
        Library.LendingTheBooks(bookname)
    elif userchoice is 3:
        returnbookname = Customer.ReturnTheBook()
        Library.AddTheBooks(returnbookname)
    elif userchoice is 4:
        quit()
