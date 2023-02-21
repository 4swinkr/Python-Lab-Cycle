from abc import ABC,abstractmethod
class Aclass(ABC): #abstract class
    @abstractmethod #decorator
    def display(self): # abstract method
         None #only the decoration no implementation

class Demo(Aclass): #concrete class
    def display(self):
        print("Abstract methods")
obj=Demo()
obj.display()