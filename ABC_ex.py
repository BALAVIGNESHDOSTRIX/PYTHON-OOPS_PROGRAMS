''' 
    @author: BALAVIGNESH M
    DATE: 28/07/2020

    Code Scope:
        To Understanding the Abstract Base Class

    Note:
        Python does not support Abstract Class but we can achieve through by uing abc module.

    Important Description About Abstract Base Class:
        -> Each ABC should have one abstract method if need more we can add and abstract method only declared. the method defenition 
           not implemented.

'''

from abc import ABC, abstractmethod

class CPU(ABC):

    @abstractmethod
    def cpuinfo(self):
        pass 


class Laptop(CPU):
    def __init__(self):
        self.lapname = "HP 637"
        self.vtx_enable = False 
        self.cpuname = "FireBelon"
        self.cpufamily = "L1BTY-TIFRIX"
        self.cpucount = 8

    def cpuinfo(self):
        print("CPU NAME" + ("*" * 10) + ">" + " " + str(self.cpuname))
        print("FAMILY  " + ("*" * 10) + ">" + " " + str(self.cpufamily))
        print("V-TX    " + ("*" * 10) + ">" + " " + str("VTX-Enabled" if self.vtx_enable else "VTX-Not Enabled"))

lap = Laptop()
lap.cpuinfo()
