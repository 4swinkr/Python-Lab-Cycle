"method overriding"
class father():
    def transportation(self):
        print("Cycle")
    
class son(father):
    def transportation(self):
        print("Bike")
        
obj=son()
obj.transportation()