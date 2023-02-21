"Encapsulation"
class encap:
    __a=10
    def __display(self):
        print("Welcome")
        print("Instance variable",self.__a)
    def show(self):
        print("this is show fn")
        self.__display()
obj=encap()
#print(obj.a)
#obj.display()
obj.show()
