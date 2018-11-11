
'''
            The class derived from more than 1 base called as a Multiple Inheritence.

Programmer_name : BALAVIGNESH.M
Implemented_Date : 11-11-2018

'''


class OS:

    SecurityOS = "Linux"
    DeveloperlikeOS = "Mac OS"
    Most_Personal_usage_OS = "Windows"

class KernerlType:

    SecurityOS_Kernel = "MonoLithic Kernel"
    DeveloperlikeOS_Kernel = "XNU Kernel"
    Most_Personal_usage_OS_Kernel = "Hybrid Kernel"

class OSINFO(OS,KernerlType):

    def __init__(self):

        self.SecurityOS_Owner = "Linus Tarvolds & maintained By Linux Foundation"
        self.DeveloperlikeOS_Owner = "Steve Jobs & Apple Inc."
        self.Most_Personal_usage_OS_Owner = "Bill Gates & Microsoft"

    def GetOSInfo(self):

        print("Most powerful Security OS is: {x}.\n Using Kernel Type: {y} .\n Developer & Owned Company is: {z}".format(
            x= self.SecurityOS , y = self.SecurityOS_Kernel , z = self.SecurityOS_Owner
        ))

        print()

        print("Most Developer and Trending OS is: {x}. \n Using Kernel Type: {y}.\n Developer & Owned Company is: {z}".format(
            x = self.DeveloperlikeOS , y = self.DeveloperlikeOS_Kernel , z = self.DeveloperlikeOS_Owner
        ))

        print()

        print("Favourite & number 1 Most user personal usage OS: {x}.\n Using Kernel Type: {y}.\n Developer & Owned Company is:{z} ".format(
            x = self.Most_Personal_usage_OS , y = self.Most_Personal_usage_OS_Kernel , z = self.Most_Personal_usage_OS_Owner
        ))

osinfo = OSINFO()
osinfo.GetOSInfo()
