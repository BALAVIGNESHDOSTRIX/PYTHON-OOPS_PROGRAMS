
'''
        Multi-level Inheritence:
            each class derived from previous class

        More Explanation:

            we have 4 class called class-1,class-2,class-3,class-4

            class-2 is derived from class-1
            class-3 is derived from class-2
            class-4 is derived from class-3

Programmer_name : BALAVIGNESH.M
Implemented_Date : 11-11-2018
'''

class Linux:


    developed_year = 1991
    base_family = "UNIX"

class Linux_Inside_Info(Linux):

    most_usage = "Server & cloud & Top MNC Database Systems"
    Kernel_type = "MonoLithic"
    multitasking_enabled = True
    varient_bases = "Debian & RedHat"
    developed_language = "C & C++"
    supporting_filesystem = "ext4 & ext3 (extended file system)"
    filesystem_supporting_storage = "1-YB (Yotta Byte)"
    Ram_consumption = "Most Linux Distro uses within 250 MB to 3-GB"
    supporting_installation = "Live Boot & Disk Installation"

class EnvironmentInfo(Linux_Inside_Info):

    environment_types = ["GNOME","xfce","KDE","KDE Plasma","MATE"]
    most_fav_env = environment_types[0]

class UsageTypeOfLinux(EnvironmentInfo):

    securityLinux = ["Arch-Linux","Kali-Linux","Parrot-Linux"]
    personaldesktoplinux = ["Ubuntu-Linux","Fedora-Linux","Open-Suse Linux"]
    ServerLinux = ["CentOS Linux","RedHat Linux"]
    BeautifulLinux = ["Deepin Linux","Elementry OS","Zorin Linux"]

class GetInfo(UsageTypeOfLinux):

    def __init__(self):
        self.developer_name = "Linus Tarvolds"

    def LinuxHistroy(self):
        print("############# LINUX HISTORY ##############")
        print()
        print("Father Of Linux: ",self.developer_name)
        print("Developed Year: ",self.developed_year)
        print("Base Family: ",self.base_family)
        print()

    def GetTechnicalInfo(self):
        print("########## Linux Technical Info ##########")
        print()
        print("Most Usage of Linux: ",self.most_usage)
        print("Most Linux Distro Kernel Type: ",self.Kernel_type)
        print("Linux supports Mulittasking option: ",self.multitasking_enabled)
        print("Available Varient Base: ",self.varient_bases)
        print("Linux Developed Language: ",self.developed_language)
        print("Linux supporting file System: ",self.supporting_filesystem)
        print("Linux filesystem supporting storage: ",self.filesystem_supporting_storage)
        print("Most Linux Distro usage RAM Size: ",self.Ram_consumption)
        print("Most Linux Supporting Installation Type: ",self.supporting_installation)
        print()

    def GetEnvironmentInfo(self):
        print("############## Linux Environment Details #############")
        for env in self.environment_types:
            print(env)
        print()

    def GetUageInfo(self):
        print("############ Usage and Security Infos #################")
        print()
        print("Security & Hacking OS Distros:")
        for sec in self.securityLinux:
            print(sec)
        print()
        print("Personal Desktop Linux Distros:")
        for desk in self.personaldesktoplinux:
            print(desk)
        print()
        print("Server Linux Distros:")
        for distro in self.ServerLinux:
            print(distro)
        print()
        print("Beautiful Linux Distros:")
        for beauti in self.BeautifulLinux:
            print(beauti)

linuxinfo = GetInfo()
linuxinfo.LinuxHistroy()
linuxinfo.GetTechnicalInfo()
linuxinfo.GetEnvironmentInfo()
linuxinfo.GetUageInfo()
